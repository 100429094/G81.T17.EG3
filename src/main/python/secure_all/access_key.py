"""Contains the class Access Key"""
import json
import os
from datetime import datetime
import hashlib
import sys
import re
from pathlib import Path
from .access_management_exception import AccessManagementException


class AccessKey:
    """Class representing the key for accessing the building"""

    def __init__(self, dni, access_code, notification_emails, validity):
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.id_document = dni
        self.access_code = access_code
        self.notification_emails = notification_emails
        justnow = datetime.utcnow()
        if "unittest" in sys.modules:
            justnow = datetime(2021, 1, 1, 1, 1)
        self.issued_at = datetime.timestamp(justnow)
        if validity == 0:
            self.__expiration_date = 0
        else:
            """timestamp is represneted in seconds.microseconds
            validity must be expressed in senconds to be added to the timestap"""
            self.__expiration_date = self.__issued_at + (validity * 24 * 60 * 60)
        self.pathJson = str(Path.cwd()) + "/../../JsonFiles/"

    def get_access_key(self, input_file):
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Archivo o ruta del archivo incorrecta") from ex
        except json.JSONDecodeError as ex:
            raise AccessManagementException("JSON Decode Error - Formato Json incorrecto") from ex
        if "DNI" not in data or "AccessCode" not in data or "NotificationMail" not in data:
            raise AccessManagementException("Etiqueta incorrecta")
        dni = data["DNI"]
        access_code = data["AccessCode"]
        notification_emails = data["NotificationMail"]
        value = AccessKey(dni, access_code, notification_emails, 2)
        value.__key = value.key

        if access_code != self.access_code:
            raise AccessManagementException("Access code erróneo")

        self.save_to_storage_key(value)

        return value.key

    def save_to_storage_key(self, value):
        my_file = self.pathJson + "storageKey.json"
        if os.path.exists(my_file):
            if os.stat(my_file).st_size == 0:
                os.remove(my_file)
                with open(my_file, "x", encoding="utf-8", newline="") as file:
                    list_data = [value.__dict__]
                    json.dump(list_data, file, indent=2)
            else:
                with open(my_file, "r", encoding="utf-8", newline="") as file:
                    list_data = json.load(file)
                    for k in list_data:
                        if k["_AccessKey__id_document"] == value.id_document:
                            raise AccessManagementException("Clave encontrada en storageRequest")
                    list_data.append(value.__dict__)
                with open(my_file, "w", encoding="utf-8", newline="") as file:
                    json.dump(list_data, file, indent=2)
        else:
            with open(my_file, "x", encoding="utf-8", newline="") as file:
                list_data = [value.__dict__]
                json.dump(list_data, file, indent=2)

    def __signature_string(self):
        """Composes the string to be used for generating the key"""
        return "{alg:"+self.__alg+",typ:"+self.__type+",accesscode:"+self.__access_code +\
               ",issuedate:"+str(self.__issued_at)+",expirationdate:"+str(self.__expiration_date)+"}"

    @property
    def id_document(self):
        """Property that represents the dni of the visitor"""
        return self.__id_document

    @id_document.setter
    def id_document(self, value):
        mensaje_excepcion_dni = "EXCEPTION: El DNI recibido no es valido o no tiene un formato valido"
        if type(value) != str:
            raise AccessManagementException(mensaje_excepcion_dni)
        if len(value) != 9:
            raise AccessManagementException(mensaje_excepcion_dni)
        if value.isdigit():
            raise AccessManagementException(mensaje_excepcion_dni)
        if value[-2:-1].isalpha():
            raise AccessManagementException(mensaje_excepcion_dni)

        letra = "TRWAGMYFPDXBNJZSQVHLCKE"
        try:
            num = int(value[0:len(value) - 1])
        except ValueError as e:
            raise AccessManagementException(mensaje_excepcion_dni)

        if value[-1] != letra[num % 23]:
            raise AccessManagementException(mensaje_excepcion_dni)

        self.__id_document = value

    @property
    def access_code(self):
        """Property that represents the access_code of the visitor"""
        return self.__access_code

    @access_code.setter
    def access_code(self, value):
        if len(value) != 32:
            raise AccessManagementException("EXCEPCION : El codigo de acceso no es valido")
        self.__access_code = value

    @property
    def notification_emails(self):
        """Property that represents the access_code of the visitor"""
        return self.__notification_emails

    @notification_emails.setter
    def notification_emails(self, value):
        if len(value) > 5 or len(value) <= 0:
            raise AccessManagementException("EXCEPCION : Numero incorrecto de correos electronicos")
        for correo in value:
            exp_reg_email = r"[A-Za-z0-9]+\@([A-Za-z0-9]+\.){1,2}[A-Za-z]+$"
            resultado = re.match(exp_reg_email, correo)

            if not resultado:
                raise AccessManagementException("EXCEPTION: El formato de correo electrónico no es válido")

        self.__notification_emails = value

    @property
    def key(self):
        """Returns the sha256 signature"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def issued_at(self):  # Convertir issue_at y expiration_date a str
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, value):
        self.__issued_at = value
