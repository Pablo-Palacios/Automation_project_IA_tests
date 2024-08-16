from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import unittest
import requests
import time
from xpaths import Login, Home, Users, Index, Areas, Main

def element_to_click(xpath):
    element = EC.element_to_be_clickable((By.XPATH, xpath))
    return element

def element_located(xpath):
    element = EC.visibility_of_element_located((By.XPATH, xpath))
    return element

scroll_down_especific = "window.scrollBy(0, 500);"
scroll_all_down = "window.scrollTo(0, document.body.scrollHeight);"



class Recorrido(unittest.TestCase):
        
    def test_principal(self):
        
            ruta = r"C:\Program Files (x86)\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = ruta
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(Login.http)
            wait = WebDriverWait(driver, 10)

            
            #LOGIN 
            time.sleep(2)
            username = wait.until(element_to_click(Login.xpath_box_email))
            username.send_keys(Main.email2)
            time.sleep(1)
            password = wait.until(element_to_click(Login.xpath_box_password))
            password.send_keys(Main.contraseña)
            time.sleep(1)
            ingresar = wait.until(element_to_click(Login.xpath_button_ingresar))
            ingresar.click()

            #TEST EXISTE TITULO IA DATA DISCOVERY
            title = wait.until(element_located(Home.xpath_title_text))
            self.assertTrue(title.is_displayed(),"no encontro el tituto")
            time.sleep(3)

            #Menu 
            #button_menu = wait.until(element_to_click(Home.xpath_menu_hamb_button))
            #button_menu.click()
            #time.sleep(1)

            #USUARIOS
            usuarios = wait.until(element_to_click(Home.xpath_button_usuarios))
            usuarios.click()

            time.sleep(3)
            #TESTS usuarios
            title_usuarios = wait.until(element_located(Users.xpath_title_users))
            #pantalla_inicial = wait.until(element_located(Users.xpath_pantalla_inicial))
            self.assertTrue(title_usuarios.is_displayed(), "No se encontro el titulo")
            #self.assertTrue(pantalla_inicial.is_displayed(), "No se encotro la pantalla inical")

            user_box = wait.until(element_to_click(Users.xpath_botton_usuario_desplegable))
            user_box.click()
            time.sleep(2)
            data_user = wait.until(element_located(Users.xpath_box_data_user))
            self.assertTrue(data_user.is_displayed(), "No encontro box data user")
            user_box.click()
            time.sleep(1)

            button_crear_user = wait.until(element_to_click(Users.xpath_button_crear_usuarios))
            button_crear_user.click()
            time.sleep(3)

            #box_input_create = wait.until(element_located(Users.Post_Put.xpath_boxs_input))
            #self.assertTrue(box_input_create.is_displayed(), "No se encontro el box de create users")

            button_rol_user = wait.until(element_to_click(Users.Post_Put.xpath_button_rol))
            button_rol_user.click()
            rol = wait.until(element_to_click(Users.Post_Put.xpath_rol_administrador))
            rol.click()
            time.sleep(1)
            input_nombre_user = wait.until(element_to_click(Users.Post_Put.xpath_input_nombre))
            input_nombre_user.send_keys("TEST")
            time.sleep(1)
            input_apellido_user = wait.until(element_to_click(Users.Post_Put.xpath_input_apellido))
            input_apellido_user.send_keys("SELENIUM")
            time.sleep(1)
            input_mail_user = wait.until(element_to_click(Users.Post_Put.xpath_input_mail))
            input_mail_user.send_keys("test@gmail.com")
            time.sleep(1)
            input_contraseña_user = wait.until(element_to_click(Users.Post_Put.xpath_input_contraseña))
            input_contraseña_user.send_keys("1234567890")
            time.sleep(1)
            input_confir_contraseña_user = wait.until(element_to_click(Users.Post_Put.xpath_input_repetir_contra))
            input_confir_contraseña_user.send_keys("1234567890")
            time.sleep(3)
            button_confirmar_user = wait.until(element_to_click(Users.Post_Put.xpath_button_confirmar_conect))
            button_confirmar_user.click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            mjs_exito_user = wait.until(element_to_click((Users.Post_Put.xpath_ventana_exito)))
            self.assertTrue(mjs_exito_user.is_displayed(), "No se encontro la ventana de exito")
            mjs_exito_user.click()
            time.sleep(1)

            #button_menu.click()

            #INDEX

            index = wait.until(element_to_click(Home.xpath_button_indexadores))
            index.click()
            time.sleep(3)

            #TEST INDEX
            title_index = wait.until(element_located(Index.xpath_title_index))
            #lista_index = wait.until(element_located(Index.xpath_index_list))
            self.assertTrue(title_index.is_displayed(), "No encotro el title index")
            #self.assertTrue(lista_index.is_displayed(), "No se encotro la lista index")

            index_box = wait.until(element_to_click(Index.xpath_box_data_index))
            index_box.click()
            time.sleep(2)

            index_data = wait.until(element_located(Index.xpath_button_index_data))
            self.assertTrue(index_data.is_displayed(), "NO se encontro la data index")
            index_box.click()
            time.sleep(1)

            # CREAR INDEXERS
            button_crear_index = wait.until(element_to_click(Index.xpath_button_crear_index))
            button_crear_index.click()
            time.sleep(3)

            button_origen_index = wait.until(element_to_click(Index.Post_Put.xpath_button_origen))
            button_origen_index.click()
            time.sleep(1)
            opcion_origen_index = wait.until(element_to_click(Index.Post_Put.xpath_opcion_origen_de_datos))
            opcion_origen_index.click()
            time.sleep(1)
            button_destino_index = wait.until(element_to_click(Index.Post_Put.xpath_button_destino))
            button_destino_index.click()
            time.sleep(1)
            opcion_destino_index = wait.until(element_to_click(Index.Post_Put.xpath_opcion_destinos_de_datos))
            opcion_destino_index.click()
            time.sleep(1)
            button_area_index = wait.until(element_to_click(Index.Post_Put.xpath_button_area))
            button_area_index.click()
            time.sleep(1)
            opcion_area_finanzas = wait.until(element_to_click(Index.Post_Put.xpath_opcion_area_finanzas))
            opcion_area_finanzas.click()
            time.sleep(1)
            input_descripcion_index = wait.until(element_to_click(Index.Post_Put.xpath_input_descripcion))
            input_descripcion_index.send_keys("Test Selenium descripcion de indexers")
            time.sleep(2)
            button_confirmar_index = wait.until(element_to_click(Index.Post_Put.xpath_button_confirmar))
            button_confirmar_index.click()
            time.sleep(3)
            mjs_exito_indexers = wait.until(element_located((Index.Post_Put.xpath_ventana_exito)))
            self.assertTrue(mjs_exito_indexers.is_displayed(), "No se encontro la ventana de exito")
            mjs_exito_indexers.click()
            time.sleep(2)


            #INDEXERS - ORIGINS
            button_origenes = wait.until(element_to_click(Index.xpath_button_origenes))
            button_origenes.click()

            time.sleep(3)

            title_origenes = wait.until(element_located(Index.Origins.xpath_title_orgines))
            box_list_origenes = wait.until(element_located(Index.Origins.xpath_origenes_list))
            self.assertTrue(title_origenes.is_displayed(), "No se encontro title origenes")
            self.assertTrue(box_list_origenes.is_displayed(), "No se encontro lista de origenes")

            origin_desplegable = wait.until(element_to_click(Index.Origins.xpath_tabla_origenes_desple))
            origin_desplegable.click()
            time.sleep(2)
            data_origen = wait.until(element_located(Index.Origins.xpath_box_data_origenes))
            self.assertTrue(data_origen.is_displayed(), "No se encontro la data del origen")
            origin_desplegable.click()
            time.sleep(1)

            button_crear_origin = wait.until(element_to_click(Index.Origins.xpath_button_crear_origen))
            button_crear_origin.click()
            time.sleep(2)

            #box_input_= wait.until(element_located(Index.Origins.Post_Put.xpath_box_input))
            #self.assertTrue(box_input.is_displayed(), "No se encontro el box input crear origenes")

            button_seleccionar_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_button_seleccionar))
            button_seleccionar_crear_origen.click()
            time.sleep(1)
            opcion_microsoft_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_opcion_microsoft_azure)).click()
            time.sleep(1)
            input_descripcion_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_descripcion))
            input_descripcion_crear_origen.send_keys("TEST SELENIUM")
            time.sleep(1)
            input_cnn_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobCNN))
            input_cnn_crear_origen.send_keys("test cnn")
            time.sleep(1)
            input_container_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobContainer))
            input_container_crear_origen.send_keys("test container")
            time.sleep(1)
            input_folder_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobFolder))
            input_folder_crear_origen.send_keys("test folder")
            time.sleep(1)
            button_confirmar_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_button_confirmar))
            time.sleep(2)
            button_confirmar_crear_origen.click()
            time.sleep(5)
            mjs_exito_origin = wait.until(element_located((Index.Destinos.Post_Put.xpath_ventana_exito)))
            self.assertTrue(mjs_exito_origin.is_displayed(), "No se encontro la ventana de exito")
            mjs_exito_origin.click()

            # INDEXERS - DESTINOS
            index = wait.until(element_to_click(Home.xpath_button_indexadores))
            index.click()
            time.sleep(2)
            button_destinos = wait.until(element_to_click(Index.xpath_button_destinos))
            button_destinos.click()

            time.sleep(3)

            title_destinos = wait.until(element_located(Index.Destinos.xpath_title_destinos))
            box_list_destinos= wait.until(element_located(Index.Destinos.xpath_destinos_list))
            self.assertTrue(title_destinos.is_displayed(), "No se encontro title destinos")
            self.assertTrue(box_list_destinos.is_displayed(), "No se encontro lista de destinos")


            destino_desplegable = wait.until(element_to_click(Index.Destinos.xpath_tabla_destinos_desple))
            destino_desplegable.click()
            time.sleep(2)
            data_destino = wait.until(element_located(Index.Destinos.xpath_box_data_destinos))
            self.assertTrue(data_destino.is_displayed(), "No se encontro la data del destino")
            destino_desplegable.click()
            time.sleep(1)


            button_crear_destino = wait.until(element_to_click(Index.Destinos.xpath_button_crear_destinos))
            button_crear_destino.click()
            time.sleep(2)

            box_input_destino = wait.until(element_located(Index.Destinos.Post_Put.xpath_box_input))
            self.assertTrue(box_input_destino.is_displayed(), "No se encontro el box input crear destino")


            button_seleccionar_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_button_seleccionar))
            button_seleccionar_destinos.click()
            time.sleep(1)
            opcion_microsoft_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_opcion_microsoft_azure))
            opcion_microsoft_destinos.click()
            time.sleep(1)
            input_descripcion_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_descripcion))
            input_descripcion_destinos.send_keys("TEST SELENIUM")
            time.sleep(1)
            input_cnn_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobCNN))
            input_cnn_destinos.send_keys("test cnn")
            time.sleep(1)
            input_container_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobContainer))
            input_container_destinos.send_keys("test container")
            time.sleep(1)
            input_folder_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobFolder))
            input_folder_destinos.send_keys("test folder")
            time.sleep(1)
            button_confirmar_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_button_confirmar))
            time.sleep(2)
            button_confirmar_destinos.click()
            time.sleep(4)

            mjs_exito_destino = wait.until(element_located((Index.Destinos.Post_Put.xpath_ventana_exito)))
            self.assertTrue(mjs_exito_destino.is_displayed(), "No se encontro la ventana de exito")
            mjs_exito_destino.click()
            time.sleep(2)

            #button_menu.click()


            #REPORTE DE BUSQUEDAS
            repor_busquedas = wait.until(element_to_click(Home.xpath_button_reportesDeBusqueda))
            repor_busquedas.click()
            time.sleep(1)
            #button_menu.click()



            #REPORTE DE INDEXADO
            repor_indexado = wait.until(element_to_click(Home.xpath_button_reportesDeIndexado))
            repor_indexado.click()
            time.sleep(1)
            #button_menu.click()



            #GESTION DE AREAS
            areas = wait.until(element_to_click(Home.xpath_button_gestion_de_areas))
            areas.click()
            time.sleep(3)

            #test areas
            title_areas = wait.until(element_located(Areas.xpath_title_areas))
            #areas_list = wait.until(element_located(Areas.xpath_areas_list))
            self.assertTrue(title_areas.is_displayed(), "No se encuentra title areas")
            #self.assertTrue(areas_list.is_displayed(), "NO se encuentra lista areas")

            areas_box_finanzas = wait.until(element_to_click(Areas.xpath_finanzas_desplegable))
            areas_box_finanzas.click()
            time.sleep(2)
            areas_data = wait.until(element_located(Areas.xpath_box_data))
            self.assertTrue(areas_data.is_displayed(), "No se encontro data area")
            #areas_box.click()
            areas_box_admi = wait.until(element_to_click(Areas.xpath_administración_desplegable))
            areas_box_admi.click()
            
            time.sleep(2)

            #button_menu.click()


            #HOME BUSQUEDA
            busqueda = wait.until(element_to_click(Home.xpath_button_busqueda))
            busqueda.click()
            time.sleep(3)

            button_fecha = wait.until(element_located(Home.xpath_button_fecha))
            button_pdf = wait.until(element_located(Home.xpath_button_pdf))
            button_img = wait.until(element_located(Home.xpath_button_imagenes))
            button_search = wait.until(element_to_click(Home.xpath_button_search))

            #tets search
            self.assertTrue(button_fecha.is_displayed(), "No se encontro el boton fecha")
            self.assertTrue(button_pdf.is_displayed(), "No se encontro el boton pdf")
            self.assertTrue(button_img.is_displayed(), "No se encontro el boton imagenes")
            button_search.click()
            time.sleep(3)









class LoginTest(unittest.TestCase):

    def test_login_fail(self):
            ruta = r"C:\Program Files (x86)\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = ruta
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(Login.http)
            wait = WebDriverWait(driver, 10)

            time.sleep(2)
            username = wait.until(element_to_click(Login.xpath_box_email))
            username.send_keys(Main.email2)
            time.sleep(1)
            password = wait.until(element_to_click(Login.xpath_box_password))
            password.send_keys("1273312")
            time.sleep(1)
            ingresar = wait.until(element_to_click(Login.xpath_button_ingresar))
            ingresar.click()

            msj_error = wait.until(element_located(Login.xpath_mjs_error))
            self.assertTrue(msj_error.is_displayed(), "No se encontro el mensaje de error de login")
            time.sleep(2)





class UsersTest(unittest.TestCase):

    def test_post(self):
         
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Users.http)
        wait = WebDriverWait(driver, 10)

        time.sleep(3)

        button_crear_user = wait.until(element_to_click(Users.xpath_button_crear_usuarios))
        button_crear_user.click()
        time.sleep(3)

        #box_input_create = wait.until(element_located(Users.Post_Put.xpath_boxs_input))
        #self.assertTrue(box_input_create.is_displayed(), "No se encontro el box de create users")

        button_rol_user = wait.until(element_to_click(Users.Post_Put.xpath_button_rol))
        button_rol_user.click()
        rol = wait.until(element_to_click(Users.Post_Put.xpath_rol_administrador))
        rol.click()
        input_nombre_user = wait.until(element_to_click(Users.Post_Put.xpath_input_nombre))
        input_nombre_user.send_keys("TEST")
        input_apellido_user = wait.until(element_to_click(Users.Post_Put.xpath_input_apellido))
        input_apellido_user.send_keys("SELENIUM")
        input_mail_user = wait.until(element_to_click(Users.Post_Put.xpath_input_mail))
        input_mail_user.send_keys("test@gmail.com")
        input_contraseña_user = wait.until(element_to_click(Users.Post_Put.xpath_input_contraseña))
        input_contraseña_user.send_keys("1234567890")
        input_confir_contraseña_user = wait.until(element_to_click(Users.Post_Put.xpath_input_repetir_contra))
        input_confir_contraseña_user.send_keys("1234567890")
        time.sleep(3)
        button_confirmar_user = wait.until(element_to_click(Users.Post_Put.xpath_button_confirmar_conect))
        button_confirmar_user.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        mjs_exito_user = wait.until(element_located((Users.Post_Put.xpath_ventana_exito)))
        self.assertTrue(mjs_exito_user.is_displayed(), "No se encontro la ventana de exito")



    def test_update_user(self):
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Users.http)
        wait = WebDriverWait(driver, 10)

        time.sleep(3)

        user_box = wait.until(element_to_click(Users.xpath_botton_usuario_desplegable))
        user_box.click()
        time.sleep(2)
        data_user = wait.until(element_located(Users.xpath_box_data_user))
        self.assertTrue(data_user.is_displayed(), "No encontro box data user")
        button_editar_user = wait.until(element_to_click(Users.xpath_button_editar))
        button_editar_user.click()
        time.sleep(4)

        button_rol = wait.until(element_to_click(Users.Post_Put.xpath_button_rol))
        button_rol.click()
        rol = wait.until(element_to_click(Users.Post_Put.xpath_rol_buscador))
        rol.click()
        input_nombre = wait.until(element_to_click(Users.Post_Put.xpath_input_nombre))
        input_nombre.clear()
        time.sleep(1)
        input_nombre.send_keys("Nahuel")
        time.sleep(1)
        input_apellido = wait.until(element_to_click(Users.Post_Put.xpath_input_apellido))
        input_apellido.clear()
        time.sleep(1)
        input_apellido.send_keys("Palacios")
        time.sleep(1)
        input_mail = wait.until(element_to_click(Users.Post_Put.xpath_input_mail))
        input_mail.clear()
        time.sleep(1)
        input_mail.send_keys("nahuelpalacios@gmail.com")
        time.sleep(1)
        input_contraseña = wait.until(element_to_click(Users.Post_Put.xpath_input_contraseña))
        input_contraseña.send_keys("1234567890")
        time.sleep(1)
        input_confir_contraseña = wait.until(element_to_click(Users.Post_Put.xpath_input_repetir_contra))
        input_confir_contraseña.send_keys("1234567890")
        time.sleep(1)
        button_confirmar = wait.until(element_to_click(Users.Post_Put.xpath_button_confirmar_conect))
        button_confirmar.click()

        mjs_exito_user_update = wait.until(element_located((Users.Post_Put.xpath_ventana_exito)))
        self.assertTrue(mjs_exito_user_update.is_displayed(), "No se encontro la ventana de exito update")

        time.sleep(5)







class IndexTest(unittest.TestCase):

    def test_indexers(self):
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Index.http)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        button_crear_index = wait.until(element_to_click(Index.xpath_button_crear_index))
        button_crear_index.click()
        time.sleep(3)

        button_origen_index = wait.until(element_to_click(Index.Post_Put.xpath_button_origen))
        button_origen_index.click()
        opcion_origen_index = wait.until(element_to_click(Index.Post_Put.xpath_opcion_origen_de_datos))
        opcion_origen_index.click()
        button_destino_index = wait.until(element_to_click(Index.Post_Put.xpath_opcion_destinos_de_datos))
        button_destino_index.click()
        button_area_index = wait.until(element_to_click(Index.Post_Put.xpath_opcion_area_finanzas))
        button_area_index.click()
        input_descripcion_index = wait.until(element_to_click(Index.Post_Put.xpath_input_descripcion))
        input_descripcion_index.send_keys("Test Selenium descripcion de indexers")
        time.sleep(2)
        button_confirmar_index = wait.until(element_to_click(Index.Post_Put.xpath_button_confirmar))
        button_confirmar_index.click()
        time.sleep(3)
        mjs_exito_indexers = wait.until(element_located((Index.Post_Put.xpath_ventana_exito)))
        self.assertTrue(mjs_exito_indexers.is_displayed(), "No se encontro la ventana de exito")
     





    def test_origenes(self):
          
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Index.http)
        wait = WebDriverWait(driver, 10)
        time.sleep(2)

        button_origenes = wait.until(element_to_click(Index.xpath_button_origenes))
        button_origenes.click()

        time.sleep(3)

        title_origenes = wait.until(element_located(Index.Origins.xpath_title_orgines))
        box_list_origenes = wait.until(element_located(Index.Origins.xpath_origenes_list))
        self.assertTrue(title_origenes.is_displayed(), "No se encontro title origenes")
        self.assertTrue(box_list_origenes.is_displayed(), "No se encontro lista de origenes")

        origin_desplegable = wait.until(element_to_click(Index.Origins.xpath_tabla_origenes_desple))
        origin_desplegable.click()
        time.sleep(2)
        data_origen = wait.until(element_located(Index.Origins.xpath_box_data_origenes))
        self.assertTrue(data_origen.is_displayed(), "No se encontro la data del origen")
        origin_desplegable.click()
        time.sleep(1)

        button_crear_origin = wait.until(element_to_click(Index.Origins.xpath_button_crear_origen))
        button_crear_origin.click()
        time.sleep(2)

        #box_input_= wait.until(element_located(Index.Origins.Post_Put.xpath_box_input))
        #self.assertTrue(box_input.is_displayed(), "No se encontro el box input crear origenes")

        button_seleccionar_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_button_seleccionar))
        button_seleccionar_crear_origen.click()
        opcion_microsoft_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_opcion_microsoft_azure)).click()
        input_descripcion_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_descripcion))
        input_descripcion_crear_origen.send_keys("TEST SELENIUM")
        input_cnn_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobCNN))
        input_cnn_crear_origen.send_keys("test cnn")
        input_container_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobContainer))
        input_container_crear_origen.send_keys("test container")
        input_folder_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_input_BlobFolder))
        input_folder_crear_origen.send_keys("test folder")
        button_confirmar_crear_origen = wait.until(element_to_click(Index.Origins.Post_Put.xpath_button_confirmar))
        time.sleep(2)
        button_confirmar_crear_origen.click()
        time.sleep(5)
        mjs_exito_origin = wait.until(element_located((Index.Destinos.Post_Put.xpath_ventana_exito)))
        self.assertTrue(mjs_exito_origin.is_displayed(), "No se encontro la ventana de exito")









    def test_destinos(self):
        
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Index.http)
        wait = WebDriverWait(driver, 10)
        time.sleep(3)

        button_destinos = wait.until(element_to_click(Index.xpath_button_destinos))
        button_destinos.click()

        time.sleep(3)

        title_destinos = wait.until(element_located(Index.Destinos.xpath_title_destinos))
        box_list_destinos= wait.until(element_located(Index.Destinos.xpath_destinos_list))
        self.assertTrue(title_destinos.is_displayed(), "No se encontro title destinos")
        self.assertTrue(box_list_destinos.is_displayed(), "No se encontro lista de destinos")


        destino_desplegable = wait.until(element_to_click(Index.Destinos.xpath_tabla_destinos_desple))
        destino_desplegable.click()
        time.sleep(2)
        data_destino = wait.until(element_located(Index.Destinos.xpath_box_data_destinos))
        self.assertTrue(data_destino.is_displayed(), "No se encontro la data del destino")
        destino_desplegable.click()
        time.sleep(1)


        button_crear_destino = wait.until(element_to_click(Index.Destinos.xpath_button_crear_destinos))
        button_crear_destino.click()
        time.sleep(2)

        box_input_destino = wait.until(element_located(Index.Destinos.Post_Put.xpath_box_input))
        self.assertTrue(box_input_destino.is_displayed(), "No se encontro el box input crear destino")


        button_seleccionar_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_button_seleccionar))
        button_seleccionar_destinos.click()
        opcion_microsoft_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_opcion_microsoft_azure))
        opcion_microsoft_destinos.click()
        time.sleep(1)
        input_descripcion_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_descripcion))
        input_descripcion_destinos.send_keys("TEST SELENIUM")
        time.sleep(1)
        input_cnn_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobCNN))
        input_cnn_destinos.send_keys("test cnn")
        time.sleep(1)
        input_container_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobContainer))
        input_container_destinos.send_keys("test container")
        time.sleep(1)
        input_folder_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_input_BlobFolder))
        input_folder_destinos.send_keys("test folder")
        time.sleep(1)
        button_confirmar_destinos = wait.until(element_to_click(Index.Destinos.Post_Put.xpath_button_confirmar))
        time.sleep(2)
        button_confirmar_destinos.click()
        time.sleep(4)

        mjs_exito_destino = wait.until(element_located((Index.Destinos.Post_Put.xpath_ventana_exito)))
        self.assertTrue(mjs_exito_destino.is_displayed(), "No se encontro la ventana de exito")



        











            

            
            

            




