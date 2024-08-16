import unittest
import requests
from main import HttpResponse, Main

class Roles(unittest.TestCase):

    def test_can_get_all(self):
        response = requests.get(Main.http + "/roles")
        self.assertEqual(response.status_code, HttpResponse.OK, "No trajo a ningun user")
        body = response.json()

        for user in body:
            assert "Id" in user
            assert "Nombre" in user       

        assert isinstance(user["Id"], int), "No trajo un dato formato int"

    def test_error_request(self):
        response = requests.get(Main.http + "/role")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "Genero get con error en url")
        