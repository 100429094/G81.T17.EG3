"""Module 3"""
import os

from . import AccessRequest
from .access_management_exception import AccessManagementException
from .access_key import AccessKey
from pathlib import Path
from datetime import datetime
import re
import os
import json


class AccessManager:
    """Class for providing the methods for managing the access to a building"""
    def __init__(self):
        self.pathJson = str(Path.cwd()) + "/../../JsonFiles/"

    """"@staticmethod
    def validate_dni(dni):
        ""RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE""
        return True"""


    @staticmethod
    def request_access_code(id_document, access_type, full_name, email_address, validity):

        ar = AccessRequest(id_document=id_document, full_name=full_name,
                           access_type=access_type, email_address=email_address, validity=validity)
        return ar.access_code

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

        key = value.get_access_key(input_file)

        return key

        """def save_to_storage_key(self, value):
        cwd = self.pathJson
        my_file = cwd + value + ".json"
        if os.path.exists(my_file):
        os.remove(my_file)
        with open(my_file, "x", encoding="utf-8", newline="") as file:
        data = {"Key": value}
        json.dump(data, file, indent=2)"""

    def open_door(self, key):

        self.check_key(key)

        my_file = self.pathJson + "/storageKey.json"
        #my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/JsonFiles/storageKey.json"
        list_key = self.read_file(my_file)

        justnow = datetime(2021, 1, 1, 1, 1)
        justnow_timestap = datetime.timestamp(justnow)

        for k in list_key:
            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"] > justnow_timestap
                                                or k["_AccessKey__expiration_date"] == "0"):
                return True
        raise AccessManagementException("Clave no encontrada o ha expirado")

    def check_key(self, key):
        regex = '[0-9a-f]{64}'
        if re.search(regex, key):
            return True
        else:
            raise AccessManagementException("Clave invalida")

    def read_file(self, my_file):
        try:
            with open(my_file, "r", encoding="utf-8", newline="")as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise AccessManagementException("Archivo incorrecto")
        except json.JSONDecodeError as ex:
            raise AccessManagementException("JSON Decode Error - Formato Json incorrecto")
        return data
