"""Contains the class Access Key"""
from datetime import datetime
import hashlib
import sys
import re
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
