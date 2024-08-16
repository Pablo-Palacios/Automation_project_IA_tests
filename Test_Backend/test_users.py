import unittest
import requests
from main import Main, HttpResponse
from faker import Faker

faker = Faker()

create_user = {
                "Nombre": faker.first_name(),
                "Apellido": faker.last_name(),
                "Mail": faker.email(),
                "Password": faker.password(length=10, special_chars=True, 
                                           digits=True, upper_case=True, lower_case=True),
                "Habilitado": 1,
                "roles": [
                        {
                        "id": 1
                        }
                        ]
                }


class Users(unittest.TestCase):

    def test_can_get_list_user(self):
        response = requests.get(Main.http + "/user")
        body = response.json()
        #print(body)
        self.assertEqual(response.status_code, HttpResponse.OK, "No conecto con endpoint Users")

        for users in body:

            assert 'Id' in users
            assert 'Nombre' in users
            assert 'Apellido' in users
            assert 'Mail' in users
            assert 'Habilitado' in users
            assert 'Roles' in users

            roles = users['Roles']
            for role in roles:
                   assert "Id" in role
                   assert "NombreRol" in role

            
    def test_can_get_user_id(self):
        gets = requests.get(Main.http + "/user")
        body_gets = gets.json()
        for x in range(0, len(body_gets)):
            id = body_gets[x]["Id"]
            response = requests.get(Main.http + f"/user/{id}")            
            self.assertEqual(response.status_code, HttpResponse.OK, "Error en get user id")
            body = response.json()    
            
            assert 'Id' in body
            assert 'Nombre' in body
            assert 'Apellido' in body
            assert 'Mail' in body
            assert 'Habilitado' in body
            assert 'roles' in body

            roles = body['roles']
            for role in roles:
                 assert "Id" in role
                 assert "NombreRol" in role
            

   
    def test_is_habilitado(self):
            id = 1
            response = requests.get(Main.http + f"/user/{id}")
            body = response.json()
            self.assertEqual(response.status_code, HttpResponse.OK, "Error en get user id")
            habilitado = body['Habilitado']
            self.assertTrue(habilitado, "no esta habilitado el user")

    def test_false_id(self):
        gets = requests.get(Main.http + "/user")
        body_gets = gets.json()
        id_exist = set(x["Id"] for x in body_gets)
        id_false = set(range(1,50))
        id = list(id_false - id_exist)[0]
        #print(id)

        response = requests.get(Main.http + f"/user/{id}")
        body = response.json()
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Error en get user id")
        self.assertEqual(body["message"], "El usuario no fue encontrado.")
        
    def test_can_post_user(self):
        response = requests.post(Main.http + "/user", json=create_user)
        self.assertEqual(response.status_code, HttpResponse.OK, "No se genero el post user")
        assert "message" in response.json()

        gets = requests.get(Main.http + "/user")
        id = set(x["Id"]for x in gets.json())
        gets_id = max(id)
        post_user = requests.get(Main.http + f"/user/{gets_id}")
        self.assertEqual(post_user.status_code, HttpResponse.OK, "no trajo el user post")
        print(post_user.json())



    def test_bad_request_post(self):
         
        user = {
                "Apellido": "test",
                "Mail": "test@gmail.com",
                "Password": "1234567890",
                "Habilitado": 1,
                "roles": [{
                            "id": 1
                        }
                    ]
        }

        response = requests.post(Main.http + "/user", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Genero el post user fallido")
        error_body = response.json()

        assert "errors" in error_body
        
        errors = error_body["errors"]
        for error in errors:
            assert "type" in error
            assert "msg" in error
            assert "path" in error
            assert "location" in error

    def test_error_password_menos_9_caracteres(self):
        user = {
                "Nombre": "test",
                "Apellido": "test",
                "Mail": "test@gmail.com",   
                "Password": "12345",
                "Habilitado": 1,
                "roles":
                  [
                    {
                        "id": 1
                    }
                  ]
                }

        response = requests.post(Main.http + "/user", json=user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "No fallo contraseña menos de 9")
        body = response.json()
        error = body["errors"]
        #print(error)
        for msg in error:
            E = msg["msg"]
            self.assertEqual(E, "La contraseña debe tener al menos 10 caracteres.", "algo paso con el msj error")



    def test_can_update_user(self):
        response = requests.post(Main.http + "/user", json=create_user)
        self.assertEqual(response.status_code, HttpResponse.OK, "No se genero el post user")
        
        gets = requests.get(Main.http + "/user")
        id = set(x["Id"]for x in gets.json())
        gets_id = max(id)

        response_id = requests.get(Main.http + f"/user/{gets_id}")
        body_user = response_id.json()
        print(body_user)


        update_user = {
                        "Nombre": faker.first_name(),
                        "Apellido": faker.last_name(),
                        "Mail": faker.email(),
                        "Password": faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True),
                        "Habilitado": 0,
                        "roles": [
                            {
                                "id": 2
                            }
                        ]
                    }
        
    
        
        response_post = requests.put(Main.http + f"/user/{gets_id}", json=update_user)
        self.assertEqual(response_post.status_code, HttpResponse.OK, "No se updateo el user")
        msg_update = response_post.json()
        assert "message" in msg_update

        response_post_body = requests.get(Main.http + f"/user/{gets_id}")
        body_user_update = response_post_body.json()
        print(body_user_update)
        

        assert body_user_update["Nombre"] != body_user["Nombre"]
        assert body_user_update["Apellido"] != body_user["Apellido"]
        assert body_user_update["Mail"] != body_user["Mail"]
        assert update_user["Password"] != create_user["Password"]
        assert body_user_update["Habilitado"] != body_user["Habilitado"]

        roles = body_user_update['roles']
        for role in roles:
            role_put_id = role["Id"] 
        rol = body_user['roles']
        for x in rol:
            role_user = x["Id"]

        assert role_put_id != role_user


    def test_bad_request_put_user(self):
        gets = requests.get(Main.http + "/user")
        id = set(x["Id"]for x in gets.json())
        gets_id = max(id)

        put_user = {
                        
                        "Apellido": "update",
                        "Mail": "test@gmail.com",
                        "Password": "1234567890",
                        "Habilitado": 0,
                        "roles": [
                            {
                                "id": 2
                            }
                        ]
                    }
        
        response = requests.put(Main.http + f"/user/{gets_id}", json=put_user)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se updateo con error en el body")
        error_body = response.json()

        assert "errors" in error_body

        for x in error_body["errors"]:
            assert "type" in x
            assert "msg" in x
            assert "path" in x
            assert "location" in x


    def test_not_found_put_user(self):
        gets = requests.get(Main.http + "/user")
        id_exist = set(x["Id"]for x in gets.json())
        id_false = set(range(0, 100))
        id = list(id_false - id_exist)[0]

        update_user = {
                        "Nombre": "update",
                        "Apellido": "update",
                        "Mail": "test@gmail.com",
                        "Password": "1234567890",
                        "Habilitado": 0,
                        "roles": [
                            {
                                "id": 2
                            }
                        ]
                    }

        response = requests.put(Main.http + f"/user/{id}", json=update_user)
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Se updateo con un user que no existe")
        assert "message" in response.json()







