"""Module 3"""
#Añadir los import necesarios para init:
#from .access_management_exception con el punto para que coja el resto de imports para test_request_access

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


