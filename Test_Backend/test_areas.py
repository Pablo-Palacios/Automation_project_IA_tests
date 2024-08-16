import unittest
import requests 
from faker import Faker
from main import HttpResponse, Main

faker = Faker()


class Arena(unittest.TestCase):

    def test_can_get_all(self):
        response = requests.get(Main.http + "/areas")
        self.assertEqual(response.status_code, HttpResponse.OK, "No trajo todas las areas")
        body = response.json()

        for user in body:
            assert "Id" in user
            assert "Nombre" in user

    def test_error_get(self):
        response = requests.get(Main.http + "/area")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "Trajo las areas incluso con erro")

    def test_can_get_area_with_id(self):
        gets = requests.get(Main.http + "/areas")
        body_gest = gets.json()
        for x in range(0, len(body_gest)):
            id = body_gest[x]["Id"]
        
            response = requests.get(Main.http + f"/areas/{id}")
            self.assertEqual(response.status_code, HttpResponse.OK, "no encontro el user")
            body = response.json()

            assert "Id" in body
            assert "Nombre" in body
            print(body)

    def test_not_found_user(self):
        gets = requests.get(Main.http + "/areas")
        body_gest = gets.json()
        id_exist = set(x["Id"] for x in body_gest)
        id_false = set(range(1,50))
        id = list(id_false - id_exist)[0]
        response = requests.get(Main.http + f"/areas/{id}")
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Trajo datos de un idArena incorrecto")
        body = response.json()
        assert "message" in body
        print(id)
    

    