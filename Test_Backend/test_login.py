import unittest
import requests
from main import Main, HttpResponse
from faker import Faker

faker = Faker()


class Login(unittest.TestCase):
    def test_conexion(self):
        response = requests.get(Main.http + "/user")
        self.assertEqual(response.status_code, HttpResponse.OK, "No conecto con endpoint Login")

    # def test_can_login_user(self):
    #     user = {"email":Main.email2,
    #             "password":Main.contraseña
    #             }
    #     response = requests.post(Main.http + "/login", json=user)
    #     self.assertEqual(response.status_code, HttpResponse.OK, "User no se logueo correctamente")
        
        
    #     response_body = response.json()
    #     #print(response_body)

    #     assert 'access_token' in response_body
    #     assert 'refresh_token' in response_body
    #     assert "user_data" in response_body
    #     assert 'message' in response_body

    #     for data in response_body:
    #         data = response_body["user_data"]
    #         #print(data)
    #         assert 'Id' in data
    #         assert 'Nombre' in data
    #         assert 'Apellido' in data
    #         assert 'Mail' in data
    #         assert 'Habilitado' in data
    #         assert 'roles' in data

    


        

    def test_empty_box_login(self):
        user = {"email":"", 
                "password":"", 
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "User se cargo sin cargar sus datos")

    def test_miss_username_login(self):
        user = {"email":"",
                 "password":Main.contraseña,
                 }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "User se cargo sin username")

    def test_miss_password_login(self):
        user = {"email":Main.email2,
                 "password":"",
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.NOT_AUTHORIZATION, "User se cargo sin password")

    def test_error_in_email_login(self):
        user = {"email":"test@gmail.com", 
                "password":Main.contraseña, 
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.NOT_AUTHORIZATION, "User se cargo con username incorrecto")

    def test_fail_arroba_email_login(self):
        user = {"email":"nahuelpalaciosgmail.com", 
                "password":Main.contraseña, 
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "User se cargo sin @")

    def test_fail_end_com_email_login(self):
        user = {"email":"nahuelpalacios@gmail", 
                "password":Main.contraseña, 
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se cargo user sin .com")

    def test_error_in_password_login(self):
        user = {"email":Main.email2,
                 "password":"testss", 
                }
        response = requests.post(Main.http + "/login", json=user)
        self.assertEqual(response.status_code, HttpResponse.NOT_AUTHORIZATION, "User se cargo con password incorrecto")


