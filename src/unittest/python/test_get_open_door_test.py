from unittest import TestCase
from src.main.python.secure_all import access_management_exception, access_manager

class TestGetOpenDoor(TestCase):

    def test_open_door(self):
        my_key = access_manager.AccessManager()
        result = my_key.get_open_door()