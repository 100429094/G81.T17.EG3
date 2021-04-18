"""Module 3"""
import os

from . import AccessRequest
from .access_management_exception import AccessManagementException
from .access_key import AccessKey
from pathlib import Path
from datetime import datetime
import re
import json


class AccessManager:
    """Class for providing the methods for managing the access to a building"""
    def __init__(self):
        self.pathJson = str(Path.cwd()) + "/../../JsonFiles/"

    @staticmethod
    def validate_dni(dni):
        """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""
        return True

    @staticmethod
    def request_access_code(self, id_document, access_type, full_name, email_address, days):
        ar = AccessRequest(id_document=id_document, full_name=full_name,
                           access_type=access_type, email_address=email_address, validity=days)
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
        # ??? self.save_to_storage_key(value.key)

        return value.key

    def save_to_storage_request(self, value):
        my_file = self.pathJson + "storageRequest.json"
        pfile = Path(my_file)
        if pfile.is_file():
            with open(my_file, "w", encoding="utf-8", newline="") as file:
                list_data = self.read_file(my_file)

                for k in list_data:
                    if k["_AccessRequest__id_document"] == value:
                        raise AccessManagementException("DNI encontrado en storageRequest")

                list_data.append(value.__dict__)
        else:
            with open(my_file, "x", encoding="utf-8", newline="") as file:
                data = [value.__dict__]
                json.dump(data, file, indent=2)
        return
        #my_file: str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/JsonFiles/storageRequest.json"
        try:
            with open(my_file, "x", encoding="utf-8", newline="") as file:
                data = [self.__dict__]
                json.dump(data, file, indent=2)
        except FileExistsError as ex:
            list_data = self.read_file(my_file)

            for k in list_data:
                if k["_AccessRequest__id_document"] == value:
                    raise AccessManagementException("DNI encontrado en storageRequest")
            list_data.append(self.__dict__)
            with open(my_file, "w", encoding="utf-8", newline="") as file:
                json.dump(list_data, file, indent=2)

    def save_to_storage_key(self, value):
        my_file = self.pathJson + "storageKey.json"
        #my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/JsonFiles/storageKey.json"
        try:
            with open(my_file, "x", encoding="utf-8", newline="") as file:
                data = [self.__dict__]
                json.dump(data, file, indent="2")
        except FileExistsError as ex:
            list_data = self.read_file(my_file)

            for k in list_data:
                if k["_AccessRequest__id_document"] == value:
                    raise AccessManagementException("Clave encontrada en storageRequest")
            list_data.append(self.__dict__)
            with open(my_file, "w", encoding="utf-8", newline="") as file:
                json.dump(list_data, file, indent="2")

    def open_door(self, key):

        self.check_key(key)

        my_file = self.pathJson + "storageKey.json"
        #my_file = str(Path.home()) + "/PycharmProjects/G81.T17.EG3/src/JsonFiles/storageKey.json"
        list_key = self.read_file(my_file)

        justnow_timestap = datetime.timestamp()

        for k in list_key:

            if k["_AccessKey__key"] == key and (k["_AccessKey__expiration_date"] > justnow_timestap
                                                or k["_AccessKey__expiration_date"] == 0):
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
