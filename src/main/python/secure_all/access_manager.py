"""Module 3"""
#Añadir los import necesarios para init:
import
from .access_management_exception import AccessManagementException
from .access_key import AccessKey
from pathlib import Path
from datetime import datetime
import re
import json

class AccessManager:
    """Class for providing the methods for managing the access to a building"""
    def __init__(self):
        pass

    @staticmethod
    def validate_dni(dni):
        """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""
        return True

    def request_access_code(self, id_document, access_type, full_name, days):
        pass

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

        return value.key

    def get_open_door(self, key):

        self.check_key(key)

        my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/main/python/secure_all/access_manager.py"
        list_key = self.read_key_file(my_file)

        justnow = datetime.utcnow()
        justnow_timestap = datetime.timestamp()

        for k in list_key:

            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"] > justnow_timestap
                                                or k["_AccessKey__expiration_date"] ==0):
                return True
            raise AccessManagementException("Clave no encontrada o ha expirado")

    def check_key(self,key):
        regex = '[0-9a-f]{64}'
        if re.search(regex, key):
            return True
        else:
            raise AccessManagementException("Clave invalida")

    def read_key_file(self, file):
        try:
            with open(file, "r", encoding="utf-8", newline="")
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Archivo incorrecto")
        except json.JSONDecodeError as ex:
            raise AccessManagementException("JSON Decode Error - Formato Json incorrecto")
        return data





