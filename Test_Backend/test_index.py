import unittest
import requests
from main import HttpResponse, Main
from faker import Faker

faker = Faker()


class Index(unittest.TestCase): 
     
    def test_get_all_indexers(self):
        response = requests.get(Main.http + "/indexers")
        self.assertEqual(response.status_code, HttpResponse.OK, "no trajo los indexers")
        body = response.json()
        #print(body[0])

        for user in body:
            assert "Id" in user
            assert "Descripcion" in user
            assert "AnalizarEntidades" in user
            assert "Habilitado" in user
            assert "NombreTipoConectorDatos" in user
            assert "area" in user
            assert "origen" in user
            assert "destino" in user
            
        for x in range(0, len(body)):
            area = body[x]["area"]
            assert "id" in area
            assert "nombre" in area

            origen = body[x]["origen"]
            assert "id" in origen
            assert "descripcion" in origen

            destino = body[x]["destino"]
            assert "id" in destino
            assert "descripcion" in destino


    def test_error_in_url(self):
        response = requests.get(Main.http + "/index")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "inicio el url con error")

    def test_error_in_url_with_space_first(self):
        response = requests.get(Main.http + "/ indexers")
        self.assertEqual(response.status_code, HttpResponse.ERROR_SERVER, "inicio el url con error")
    
    def test_get_indexers_id(self):
        gets = requests.get(Main.http + "/indexers")
        body_gets = gets.json()
        for x in range(0, len(body_gets)):
            id = body_gets[x]["Id"]
            response = requests.get(Main.http + f"/indexers/{id}")
            self.assertEqual(response.status_code, HttpResponse.OK, "No trajo el indexers del id")
            body = response.json()
            

            assert "Id" in body
            assert "Descripcion" in body
            assert "IdDatosOrigenes" in body
            assert "IdDatosDestinos" in body
            assert "IdAreas" in body
            assert "AnalizarEntidades" in body
            assert "Habilitado" in body


    # def test_can_get_false_id(self):
    #     gets = requests.get(Main.http + "/indexers")
    #     body_gets = gets.json()
    #     id_exist = set(x["Id"] for x in body_gets)
    #     id_false = set(range(1,50))
    #     id = list(id_false - id_exist)[0]
    #     response = requests.get(Main.http + f"/indexers/{id}")
    #     self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Trajo indexers de id incorrecto")
    #     body = response.json()
    #     mjs = body["message"]
    #     self.assertEqual(mjs, "El Indexador no fue encontrado.", "no coincide el mensaje de error")
    #     print(id)

    def test_can_post_index(self):
        create_index = {
                        "Descripcion": "Test Indexado",
                        "IdDatosOrigenes": 1,
                        "IdDatosDestinos": 1,
                        "IdAreas": 1,
                        "AnalizarEntidades": 1,
                        "Habilitado": 1
                    }
        response = requests.post(Main.http + "/indexers", json=create_index)
        self.assertEqual(response.status_code, HttpResponse.OK, "No se genero el post en index")
        assert "message" in response.json()

        gets = requests.get(Main.http + "/indexers")
        all_id = set(x["Id"]for x in gets.json())
        id = max(all_id)

        post_id = requests.get(Main.http + f"/indexers/{id}")
        body_response = post_id.json()

        assert "Id" in body_response
        assert "Descripcion" in body_response
        assert "IdDatosOrigenes" in body_response
        assert "IdDatosDestinos" in body_response
        assert "IdAreas" in body_response
        assert "AnalizarEntidades" in body_response
        assert "Habilitado" in body_response

    def test_bad_request_post(self):
        create_index = {
                        
                        "IdDatosOrigenes": 1,
                        "IdDatosDestinos": 1,
                        "IdAreas": 1,
                        "AnalizarEntidades": 1,
                        "Habilitado": 1
                    }
        
        response = requests.post(Main.http + "/indexers", json=create_index)
        body_error = response.json()
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se genero un post con un bad request")
        assert "errors" in body_error
        for x in body_error["errors"]:
            assert "type" in x
            assert "msg" in x
            assert "path" in x
            assert "location" in x

        
    def test_can_update_index(self):
        create_index = {
                        "Descripcion": "Test Indexado",
                        "IdDatosOrigenes": 1,
                        "IdDatosDestinos": 1,
                        "IdAreas": 1,
                        "AnalizarEntidades": 1,
                        "Habilitado": 1
                    }
        post = requests.post(Main.http + "/indexers", json=create_index)
        self.assertEqual(post.status_code, HttpResponse.OK, "No se genero el post en index")

        gets = requests.get(Main.http + "/indexers")
        all_id = set(x["Id"]for x in gets.json())
        id = max(all_id)

        post_id = requests.get(Main.http + f"/indexers/{id}")
        self.assertEqual(post_id.status_code, HttpResponse.OK, "No trajo el indexers del id")
        original_data = post_id.json()


        update_index = {
                        "Descripcion": "UPdate Indexado",
                        "IdDatosOrigenes": 2,
                        "IdDatosDestinos": 1, 
                        "IdAreas": 2,
                        "AnalizarEntidades": 0,
                        "Habilitado": 0
                                            }
        
        response = requests.put(Main.http + f"/indexers/{id}", json=update_index)
        self.assertEqual(response.status_code, HttpResponse.OK, "No se genero el update correcto")
        assert "message" in response.json() 

        put_id = requests.get(Main.http + f"/indexers/{id}")
        self.assertEqual(put_id.status_code, HttpResponse.OK, "No trajo el indexers del id")
        updated_data = put_id.json()

        assert original_data["Descripcion"] != updated_data["Descripcion"], "La descripción no se actualizó correctamente"
        assert original_data["IdDatosOrigenes"] != updated_data["IdDatosOrigenes"], "El IdDatosOrigenes no se actualizó correctamente"
        #assert original_data["IdDatosDestinos"] != updated_data["IdDatosDestinos"], "El IdDatosDestinos no se actualizó correctamente"
        assert original_data["IdAreas"] != updated_data["IdAreas"], "El IdAreas no se actualizó correctamente"
        assert original_data["AnalizarEntidades"] != updated_data["AnalizarEntidades"], "AnalizarEntidades no se actualizó correctamente"
        assert original_data["Habilitado"] != updated_data["Habilitado"], "Habilitado no se actualizó correctamente"

    def test_bad_request_put(self):
        gets = requests.get(Main.http + "/indexers")
        ids = set(x["Id"]for x in gets.json())
        id = max(ids)

        update_index = {
                        
                        "IdDatosOrigenes": 2,
                        "IdDatosDestinos": 1, 
                        "IdAreas": 2,
                        "AnalizarEntidades": 0,
                        "Habilitado": 0
                                            }
        response = requests.put(Main.http + f"/indexers/{id}", json=update_index)
        self.assertEqual(response.status_code, HttpResponse.BAD_REQUEST, "Se genero un update con un bad request")
        body_error = response.json()
        assert "errors" in body_error
        for x in body_error["errors"]:
            assert "type" in x
            assert "msg" in x
            assert "path" in x
            assert "location" in x

    def test_not_found_index_put(self):
        gets = requests.get(Main.http + "/indexers")
        id_exits = set(x["Id"]for x in gets.json())
        id_false = set(range(0, 100))
        id = list(id_false - id_exits)[0]

        update_index = {
                        "Descripcion": "UPdate Indexado",
                        "IdDatosOrigenes": 2,
                        "IdDatosDestinos": 1, 
                        "IdAreas": 2,
                        "AnalizarEntidades": 0,
                        "Habilitado": 0
                                            }

        response = requests.put(Main.http + f"/indexers/{id}", json=update_index)
        self.assertEqual(response.status_code, HttpResponse.NOT_FOUND, "Se updateo un index que no existe")
        assert "message" in response.json()

    


        
        

        









        
