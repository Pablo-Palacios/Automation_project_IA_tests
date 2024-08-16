from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import unittest
import requests
import time
from xpaths import Login, Home, Users
                                        
#http = "http://localhost:5173/"



class LoginPage(unittest.TestCase):

    def test_a_can_sends_keys_to_login(self):

        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.get(Login.http)
        wait = WebDriverWait(driver, 10)
        

        username = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_box_email)))
        username.send_keys("ivanadelgado@gmail.com")

        password = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_box_password)))
        password.send_keys("1234")

        ingresar = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_button_ingresar)))
        ingresar.click()

        title = wait.until(EC.visibility_of_element_located((By.XPATH, Home.xpath_title_text)))

        self.assertEqual(title.text, "IA DATA DISCOVERY","no encontro el tituto")
        #print(title.text)
        #self.assertTrue(Home.xpath_menu_hamb_button, "no encontro menu hamburguesa")

        boton = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_menu_hamb_button)))
        boton.click()
        

        time.sleep(3)


    def test_b_fail_login(self):

        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.get(Login.http)
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_box_email)))
        username.send_keys("nahuel")

        password = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_box_password)))
        password.send_keys("1234")

        ingresar = wait.until(EC.element_to_be_clickable((By.XPATH, Login.xpath_button_ingresar)))
        ingresar.click()
        message = wait.until(EC.visibility_of_element_located((By.XPATH, Login.xpath_mjs_error)))

        self.assertEqual(message.text, "Datos Incorrectos", "mensaje de error no coincide")

        time.sleep(3)

         

class HomePage(unittest.TestCase):

    def test_c_titles_menu(self):
        
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.get(Home.http_search)

        #box_search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_box_search)))
        
        #box_search = driver.find_element(By.XPATH, Home.xpath_box_search)
        # MENU DESPLEGABLE

        button_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Home.xpath_menu_hamb_button)))
        button_menu.click()
        busqueda = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_button_busqueda)))
        usuarios = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_button_usuarios)))
        indexadores = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_button_indexadores)))
        reporte_busq = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_button_reportesDeBusqueda)))
        reporte_index = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Home.xpath_button_reportesDeIndexado)))

        self.assertTrue(Home.xpath_box_search, "No encontro el buscador")
        self.assertTrue(button_menu, "No se encontro el boton de menu")
        self.assertEqual(busqueda.text, "BUSQUEDA", "No coincide titulo de busqueda")
        self.assertEqual(usuarios.text, "USUARIOS", "No coincide titulo de usuarios")
        self.assertEqual(indexadores.text, "INDEXADORES", "No coincide titulo de indexadores")
        self.assertEqual(reporte_busq.text, "REPORTE DE BÚSQUEDAS", "No coincide titulo de reporte de buscadores")
        self.assertEqual(reporte_index.text, "REPORTE DE INDEXADO", "No coincide en titulo de reporte de index")

        time.sleep(3)

    def test_d_funtions_all_buttons_menu(self):
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.get(Home.http_search)
        wait = WebDriverWait(driver, 10)

        button_menu = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_menu_hamb_button)))
        button_menu.click()
        button_usuarios = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_usuarios)))
        button_usuarios.click()
        button_menu.click()
        time.sleep(3)
        button_menu.click()
        button_indexadores = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_indexadores)))
        button_indexadores.click()
        button_menu.click()
        time.sleep(3)
        button_menu.click()
        button_reportes_busqueda = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_reportesDeBusqueda)))
        button_reportes_busqueda.click()
        button_menu.click()
        time.sleep(3)
        button_menu.click()
        button_reportes_index = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_reportesDeIndexado)))
        button_reportes_index.click()
        button_menu.click()
        time.sleep(3)
        button_menu.click()
        button_areas = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_gestion_de_areas)))
        button_areas.click()
        time.sleep(3)
        button_menu.click()
        button_busqueda = wait.until(EC.element_to_be_clickable((By.XPATH, Home.xpath_button_busqueda)))
        button_busqueda.click()
        button_menu.click()
        time.sleep(3)
    

    
class UsuariosPage(unittest.TestCase):

    def test_e_check_elements_of_page(self):
        ruta = r"C:\Program Files (x86)\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = ruta
        driver = webdriver.Chrome()
        driver.get(Users.http)
        wait = WebDriverWait(driver, 10)

        title_usuarios = wait.until(EC.visibility_of_element_located((By.XPATH, Users.xpath_title_users)))
        button_user = wait.until(EC.element_to_be_clickable((By.XPATH, Users.xpath_botton_usuario_desplegable))).click()
        box_data_user = wait.until(EC.visibility_of_element_located((By.XPATH, Users.xpath_box_data_user)))

        self.assertEqual(title_usuarios.text, "Lista de Usuarios", "No coincide texto del titulo")
        self.assertTrue(box_data_user.is_displayed(), "No encontro los datos del usuario")
        time.sleep(2)

        

        
# class IndexadoresPage(unittest.TestCase):
    
#     def test_f_check_elements_page(self):
        
        


