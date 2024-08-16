import unittest
import requests
from main import HttpResponse, Main

class Connections_Type(unittest.TestCase):

    def test_can_get_all(self):
        response = requests.get(Main.http + "/connection-type")
        self.assertEqual(response.status_code, HttpResponse.OK, "No me trajo las conexiones")
        body = response.json()

        for connect in body:
            assert "Id" in connect
            assert "Nombre" in connect

    def test_get_error(self):
        response = requests.get(Main.http + "/connection")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "Trajo las conexiones igual")
        