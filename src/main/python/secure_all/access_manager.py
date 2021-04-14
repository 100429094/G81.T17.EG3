"""Module 3"""
#Añadir los import necesarios para init:
from .access_management_exception import AccessManagementException
from .access_key import AccessKey
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





