import unittest
import requests
from faker import Faker
from main import HttpResponse, Main

faker = Faker()



create_body = {
    "IdTipoConectorDatos": 1,
    "Descripcion":"test " + faker.word(),
    "BlobCNN":"test connector " + faker.word(),
    "BlobContainer":"test container " + faker.word(),
    "BlobFolder":"test folder " + faker.word()
}



class Origins(unittest.TestCase):

    def test_get_all_origins(self):
        response = requests.get(Main.http + "/origins")
        self.assertEqual(response.status_code, HttpResponse.OK, "No trajo los origins")
        body = response.json()

        for user in body:
            assert "Id" in user
            assert "Descripcion" in user
            assert "BlobCNN" in user
            assert "BlobContainer" in user
            assert "BlobFolder" in user
            assert "TipoConectorDatos" in user

    def test_error_url(self):
        response = requests.get(Main.http + "/origin")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "Trajo origins con erro en la llamada")

    def test_error_in_url_with_space_first(self):
        response = requests.get(Main.http + "/ origins")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "inicio el url con error")

    def test_get_origins_id(self):
        gets = requests.get(Main.http + "/origins")
        get_response = gets.json()
        lens= len(get_response)
        print(lens)
        for i in range(0, len(get_response)):
            ids = get_response[i]["Id"]
            #id = ids["Id"]
            #print(ids)
            
            response = requests.get(Main.http + f"/origins/{ids}")
            self.assertEqual(response.status_code, HttpResponse.OK, "No trajo los datos del id")
            body = response.json()
            #print(body)
            assert "Id" in body
            assert "IdTipoConectorDatos" in body
            assert "Descripcion" in body
            assert "BlobCNN" in body
            assert "BlobContainer" in body
            assert "BlobFolder" in body

    def test_can_get_origins_false_id(self):
        gets = requests.get(Main.http + "/origins")
        get_response = gets.json()
        id_exis = set(x["Id"] for x in get_response)
        id_false = set(range(1,100))
        id = list(id_false - id_exis)[0]

        response = requests.get(Main.http + f"/origins/{id}")
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "trajo el origins con falso id")
        body = response.json()
        mjs = body["message"]
        self.assertTrue(mjs, "No coincide el mensaje de error")

    def test_can_get_origins_with_string(self):
        string = "f"
        response = requests.get(Main.http + f"/origins/{string}")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "se formulo el get con un caracter diferente")

    def test_can_post_origin(self):
        response = requests.post(Main.http + "/origins", json= create_body)
        self.assertEqual(response.status_code, HttpResponse.OK, "No se genero el post")
        body = response.json()
        assert "message" in body

        gets = requests.get(Main.http + "/origins")
        get_response = gets.json()
        id_exist = set(x["Id"]for x in get_response)
        id = max(id_exist)
            
        get_post = requests.get(Main.http + f"/origins/{id}")
        self.assertEqual(get_post.status_code, HttpResponse.OK, f"No trajo los datos del id:{id}")

    def test_bad_request_post(self):
        bad_body = {
                        
                        "Descripcion":"test " + faker.word(),
                        "BlobCNN":"test connector " + faker.word(),
                        "BlobContainer":"test container " + faker.word(),
                        "BlobFolder":"test folder " + faker.word()
                    }
        
        response = requests.post(Main.http + "/origins", json=bad_body)
        body_response = response.json()
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se genero el post con un bad request")
        assert "errors" in body_response

        errors = body_response["errors"]
        for error in errors:
            assert "type" in error
            assert "msg" in error
            assert "path" in error
            assert "location" in error



    def test_can_put_update(self):
        gets = requests.get(Main.http + "/origins")
        get_response = gets.json()
        id_exist = set(x["Id"]for x in get_response)
        id = max(id_exist)

        response_get = requests.get(Main.http + f"/origins/{id}")
        body_user = response_get.json()
        #print(body_user)

        update_body = {
            "IdTipoConectorDatos": 1,
            "Descripcion":"update test " + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }
       
        update_response = requests.put(Main.http + f"/origins/{id}", json=update_body)
        self.assertEqual(update_response.status_code, HttpResponse.OK, "No se update correcto")
        msg = update_response.json()
        assert "message" in msg

        response_put = requests.get(Main.http + f"/origins/{id}")
        body_user_update = response_put.json()
        #print(body_user_update)

        assert body_user_update["Descripcion"] != body_user["Descripcion"]
        assert body_user_update["BlobCNN"] != body_user["BlobCNN"]
        assert body_user_update["BlobContainer"] != body_user["BlobContainer"]
        assert body_user_update["BlobFolder"] != body_user["BlobFolder"]


    def test_bad_request_put(self):
        gets = requests.get(Main.http + "/origins")
        get_response = gets.json()
        id_exist = set(x["Id"]for x in get_response)
        id = max(id_exist)

        bad_body = {
            
            "Descripcion":"update test " + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }

        update_response = requests.put(Main.http + f"/origins/{id}", json=bad_body)
        self.assertEqual(update_response.status_code, HttpResponse.BAD_REQUEST, "se updateo con un bad request")
        body_error = update_response.json()
        assert "errors" in body_error

        errors = body_error["errors"]
        for error in errors:
            assert "type" in error
            assert "msg" in error
            assert "path" in error
            assert "location" in error

    def test_not_found_put(self):
        gets = requests.get(Main.http + "/origins")
        id_exis = set(x["Id"]for x in gets.json())
        id_false = set(range(0, 100))
        id = list(id_false - id_exis)[0]

        update_body = {
            "IdTipoConectorDatos": 1,
            "Descripcion":"update test " + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }

        response = requests.put(Main.http + f"/origins/{id}", json=update_body)
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Se updateo un user que no existe")
        assert "message" in response.json()