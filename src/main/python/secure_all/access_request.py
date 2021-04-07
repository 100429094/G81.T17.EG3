"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
import sys
import re
from datetime import datetime


'''Hacer el árbol de derivacion y comprobaciones necesarias para cada str pasado'''


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

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def full_name(self):
        """Property representing the name and the surname of
        the person who request access to the building"""
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        exp_reg = "^[A-Za-z]+(\s[A-Za-z]+){1,2}$"

        resultado = re.match(exp_reg, value)

        if not resultado:
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_NAME}")

        self.__full_name = value

    @property
    def visitor_type(self):
        """Property representing the type of visitor: Resident or Guest"""
        return self.__visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        if value != "Guest" and value != "Resident":
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_ACCESS_TYPE}")
        self.__visitor_type = value

    @property
    def email_address(self):
        """Property representing the requester's email address"""
        return self.__email_address

    @email_address.setter
    def email_address(self, value):
        self.__email_address = value

    @property
    def id_document(self):
        """Property representing the requester's DNI"""
        return self.__id_document

    @id_document.setter
    def id_document(self, value):
        if type(value) != str:
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if len(value) != 9:
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if value.isdigit():
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")
        if value[-2:-1].isalpha():
            from secure_all import AccessManagementException
            raise AccessManagementException(f"{self.MENSAJE_EXCEPCION_DNI}")

        letra = "TRWAGMYFPDXBNJZSQVHLCKE"
        try:
            num = int(value[0:len(value)-1])
        except ValueError as e:
            from secure_all import AccessManagementException
            raise AccessManagementException("EXCEPTION: id_card debe tener 9 caracteres")

        if value[-1] != letra[num%23]:
            from secure_all import AccessManagementException
            raise AccessManagementException("EXCEPTION: id_card debe tener 9 caracteres")

        self.__id_document = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def access_code(self):
        """Returns the md5 signature"""
        #Validar la lista de valores pasados
        return hashlib.md5(self.__str__().encode()).hexdigest()
