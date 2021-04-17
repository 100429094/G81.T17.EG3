"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
import os
import sys
import re
from pathlib import Path
from datetime import datetime
from .access_management_exception import AccessManagementException


class AccessRequest:
    """Class representing the access request"""
    MENSAJE_EXCEPCION_DNI = "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido"
    MENSAJE_EXCEPCION_ACCESS_TYPE = "EXCEPTION: El tipo de acceso solicitado no es valido"
    MENSAJE_EXCEPCION_NAME = "EXCEPTION: La cadena de nombre y apellido no es válida"
    MENSAJE_EXCEPCION_EMAIL = "EXCEPTION: El formato de correo electrónico no es válido"
    MENSAJE_EXCEPCION_VALIDITY = "EXCEPTION: El número de días no tiene un valor válido"
    MENSAJE_EXCEPCION_OTHER = "EXCEPTION: Otros errores internos"

    def __init__(self, id_document, full_name, access_type, email_address, validity):
        self.id_document = id_document
        self.full_name = full_name
        self.visitor_type = access_type
        self.email_address = email_address
        self.validity = validity
        justnow = datetime.utcnow()
        if "unittest" in sys.modules:
            justnow = datetime(2021, 1, 1, 1, 1)
        self.__time_stamp = datetime.timestamp(justnow)
        self.save_to_storage_key()

    def save_to_storage_key(self):
        cwd = str(Path.cwd()) + "/../../../JsonFilesRequests/"
        my_file = cwd + self.id_document + ".json"
        pfile = Path(my_file)
        if os.path.exists(my_file):
            os.remove(my_file)
        with open(my_file, "x", encoding="utf-8", newline="") as file:
            data = []
            data.append({"AccessCode": self.access_code,
                        "DNI": self.id_document,
                        "NotificationMail": self.email_address}
                        )
            json.dump(data, file, indent=2)


    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def full_name(self):
        """Property representing the name and the surname of
        the person who request access to the building"""
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        exp_reg_name = "^[A-ZÁÉÍÓÚa-záéíóú]+(\s[A-ZÁÉÍÓÚa-záéíóú]+){1,2}$"
        resultado = re.match(exp_reg_name, value)

        if not resultado:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_NAME}")

        self.__full_name = value

    @property
    def visitor_type(self):
        """Property representing the type of visitor: Resident or Guest"""
        return self.__visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        if value != "Guest" and value != "Resident":
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_ACCESS_TYPE}")
        self.__visitor_type = value

    @property
    def validity(self):
        """Property representing the validity of visitor"""
        return self.__validity

    @validity.setter
    def validity(self, value):
        if self.__visitor_type == "Guest":
            if value < 2 or value > 15:
                raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_VALIDITY}")
        if self.__visitor_type == "Resident":
            if value != 0:
                raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_VALIDITY}")
        self.__validity = value

    @property
    def email_address(self):
        """Property representing the requester's email address"""
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        # 100429094@alumnos.uc3m.es
        exp_reg_email = "[A-Za-z0-9]+\@([A-Za-z0-9]+\.){1,2}[A-Za-z]+$"
        resultado = re.match(exp_reg_email, value)

        if not resultado:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_EMAIL}")

        self.__email_address = value

    @property
    def id_document(self):
        """Property representing the requester's DNI"""
        return self.__id_document

    @id_document.setter
    def id_document(self, value):
        if type(value) != str:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if len(value) != 9:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if value.isdigit():
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if value[-2:-1].isalpha():
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")

        letra = "TRWAGMYFPDXBNJZSQVHLCKE"
        try:
            num = int(value[0:len(value)-1])
        except ValueError as e:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")

        if value[-1] != letra[num % 23]:
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")

        self.__id_document = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def access_code(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()
