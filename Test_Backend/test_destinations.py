import unittest
import requests
from main import HttpResponse, Main
from faker import Faker

faker = Faker()

create_body = {
    "IdTipoConectorDatos": 1,
    "Descripcion":"test " + faker.word(),
    "BlobCNN":"test connector " + faker.word(),
    "BlobContainer":"test container " + faker.word(),
    "BlobFolder":"test folder " + faker.word()
}

class Destinations(unittest.TestCase):

    def test_can_get_all(self):
        response = requests.get(Main.http + "/destinations")
        self.assertEqual(response.status_code, HttpResponse.OK, "No se trajo los datos")
        body = response.json()
        
        for user in body:
            assert "Id" in user
            assert "Descripcion" in user
            assert "BlobCNN" in user
            assert "BlobContainer" in user
            assert "BlobFolder" in user
            assert "Nombre" in user 
  

    def test_error_get_all(self):
        response = requests.get(Main.http + "/destination")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "No se trajo los datos")

    def test_can_get_id(self):
        response = requests.get(Main.http + "/destinations")
        self.assertEqual(response.status_code, HttpResponse.OK, "No se trajo los datos")
        gets_id = response.json()
        for i in range(0, len(gets_id)):
            id = gets_id[i]["Id"]
            
            response = requests.get(Main.http + f"/destinations/{id}")
            self.assertEqual(response.status_code, HttpResponse.OK, "No se trajo los datos")
            body = response.json()
            

            assert "Id" in body
            assert "IdTipoConectorDatos" in body
            assert "Descripcion" in body
            assert "BlobCNN" in body
            assert "BlobContainer" in body
            assert "BlobFolder" in body
        
    def test_get_not_found_id(self):
        response = requests.get(Main.http + "/destinations")
        gets_id = response.json()
        id_exist = set(x["Id"] for x in gets_id)
        id_false = set(range(1,50))
        id = list(id_false - id_exist)[0]
        print(id)
        response = requests.get(Main.http + f"/destinations/{id}")
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND)
        msj = response.json()

        assert "message" in msj

    def test_can_post(self):
        response = requests.post(Main.http + "/destinations", json=create_body)
        self.assertEqual(response.status_code, HttpResponse.OK)

        gets = requests.get(Main.http + "/destinations")
        gets_body = gets.json()
        id_exist = set(x["Id"]for x in gets_body)
        id = max(id_exist)
        response_id = requests.get(Main.http + f"/destinations/{id}")
        self.assertEqual(response_id.status_code, HttpResponse.OK, "No se encontro el id")
        #print(response_id.json())
        body = response_id.json()
            
        assert "Id" in body
        assert "IdTipoConectorDatos" in body
        assert "Descripcion" in body
        assert "BlobCNN" in body
        assert "BlobContainer" in body
        assert "BlobFolder" in body

    def test_bad_request_post(self):
        bad_body = {
            
            "Descripcion":"update" + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }

        response = requests.post(Main.http + "/destinations", json=bad_body)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se creo destination con bad request")
        body_error = response.json()

        assert "errors" in body_error

        errors = body_error["errors"]
        for error in errors:
            assert "type" in error
            assert "msg" in error
            assert "path" in error
            assert "location" in error

    def test_can_put_id(self):
        response = requests.post(Main.http + "/destinations", json=create_body)
        self.assertEqual(response.status_code, HttpResponse.OK)

        gets = requests.get(Main.http + "/destinations")
        gets_body = gets.json()
        id_exist = set(x["Id"]for x in gets_body)
        id = max(id_exist)

        response_get = requests.get(Main.http + f"/destinations/{id}")
        self.assertEqual(response_get.status_code, HttpResponse.OK, "No se encontro el id")
        body_get = response_get.json()

        update_body = {
            "IdTipoConectorDatos": 1,
            "Descripcion":"update" + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }               
        update_response = requests.put(Main.http + f"/destinations/{id}", json=update_body)
        self.assertEqual(update_response.status_code, HttpResponse.OK, "No se update")
        assert "message" in update_response.json()

        response_put = requests.get(Main.http + f"/destinations/{id}")
        self.assertEqual(response_put.status_code, HttpResponse.OK, "No se encontro el id")
        body_put = response_put.json()

        assert body_put["Descripcion"] != body_get["Descripcion"]
        assert body_put["BlobCNN"] != body_get["BlobCNN"]
        assert body_put["BlobContainer"] != body_get["BlobContainer"]
        assert body_put["BlobFolder"] != body_get["BlobFolder"]


    def test_bad_request_put(self):
        gets = requests.get(Main.http + "/destinations")
        gets_body = gets.json()
        id_exist = set(x["Id"]for x in gets_body)
        id = max(id_exist)

        update_body = {
            
            "Descripcion":"update" + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }  
        
        update_response = requests.put(Main.http + f"/destinations/{id}", json=update_body)
        self.assertEqual(update_response.status_code, HttpResponse.BAD_REQUEST, "se updatea un destinations con un bad request")
        body_error = update_response.json()
        assert "errors" in body_error

        errors = body_error["errors"]
        for error in errors:
            assert "type" in error
            assert "msg" in error
            assert "path" in error
            assert "location" in error

    def test_not_found_id_put(self):
        gets = requests.get(Main.http + "/destinations")
        id_exist = set(x["Id"]for x in gets.json())
        id_false = set(range(0, 1000))
        id = list(id_false - id_exist)[0]

        update_body = {
            "IdTipoConectorDatos": 1,
            "Descripcion":"update" + faker.word(),
            "BlobCNN":"update connector " + faker.word(),
            "BlobContainer":"update container " + faker.word(),
            "BlobFolder":"update folder " + faker.word()
        }  

        update_response = requests.put(Main.http + f"/destinations/{id}", json=update_body)
        self.assertEqual(update_response.status_code, HttpResponse.NOT_FOUND, "se updatea un destinations que no existe")
        body_error = update_response.json()
        assert "message" in body_error


        
