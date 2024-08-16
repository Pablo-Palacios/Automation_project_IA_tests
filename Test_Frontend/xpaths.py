class Main():
    email1 ="nahuelpalacios@gmail.com"
    email2= "ivanadelgado@gmail.com"
    contraseña = "1234"

class Login():
    http = "http://localhost:5173/"

    #Xpathss
    xpath_imagen_logo = "//div/img[@class='sc-hLQSwg gsqiEL']"
    xpath_box_email = "//div[@class='sc-fsYfdN iViKJA']/input[@type='email']"
    xpath_box_password = "//div[@class='sc-fsYfdN iViKJA']/input[@type='password']"
    xpath_button_ingresar = "//div[@class='sc-gLLuof gubBQq']/button"
    xpath_button_login_google = "//button/text[text()='Ingresar con Google']"
    xpath_button_login_microsoft = "//button/text[text()='Ingresar con Microsoft']"
    xpath_mjs_error = "//p[@class = 'sc-irLvIq fsWuDG']"

    

class Home():
    http_search = "http://localhost:5173/search"

    #Xpaths
    xpath_title_text = "//div[text()='IA DATA DISCOVERY']"
    xpath_input_box_search = "//input[@class='sc-drMgrp fmqidQ']"
    xpath_menu_hamb_button = "//div[@class='sc-khjJXk gUshKN']"
    xpath_button_busqueda = "//a[text()='BUSQUEDA']"
    xpath_button_usuarios = "//a[text()='USUARIOS']"
    xpath_button_indexadores = "//a[text()='INDEXADORES']"
    xpath_button_reportesDeBusqueda = "//a[text()='REPORTE DE BÚSQUEDAS'] "
    xpath_button_reportesDeIndexado = "//a[text()='REPORTE DE INDEXADO']"
    xpath_button_gestion_de_areas = "//a[text()='GESTIÓN DE AREAS']"
    xpath_button_search = "//button[text()='Search']"
    xpath_button_fecha = "//button[text()='Fecha']"
    xpath_button_pdf = "//button[text()='Pdf']"
    xpath_button_imagenes = "//button[text()='Imagenes']"
   


class Users():
    http = "http://localhost:5173/users"

    #Xpaths
    xpath_title_users = "//text[text()='Lista de Usuarios']"
    xpath_botton_usuario_desplegable = "//div[@class='sc-eAKtBH djJGJI']"
    xpath_box_data_user = "//div[@class='sc-kMzELR enAosP']"
    xpath_button_crear_usuarios = "//button[@class='sc-cCzLxZ jErGNF']"
    xpath_pantalla_inicial = "//div[@class='sc-fLseNd hqXmnK']"
    xpath_button_editar = "//a[@class='sc-hhyKGa eoyvXd']"
    xpath_box_user_update = "//div[@class='sc-eAKtBH djJGJI']"

    class Post_Put():
        xpath_button_rol = "//button[text()='Rol']"
        xpath_rol_administrador = "//text[text()='Administrador']"
        xpath_rol_buscador = "//text[text()='Buscador']"
        xpath_input_nombre = "//input[@placeholder='Nombre']"
        xpath_input_apellido = "//input[@placeholder='Apellido']"
        xpath_input_mail = "//input[@placeholder='Mail']"
        xpath_input_contraseña = "//input[@placeholder='Contraseña']"
        xpath_input_repetir_contra = "//input[@placeholder='Repetir Contraseña']"
        xpath_checkbox_habilitado = "//button[@class='sc-kGLCbq lnhsvY']"
        xpath_button_confirmar_desconectado= "//button[@class='sc-jPQKUW jdCJQF']"
        xpath_button_confirmar_conect = "//button[text()='Confirmar']"
        xpath_boxs_input = "//div[@class='sc-faxByu fGLnjh']"
        xpath_ventana_exito = "//div[@class='sc-cmfnrN ejoJGS']/button"
        



class Index():
    http = "http://localhost:5173/indexers"

    #Xpaths
    xpath_title_index = "//text[text()='Gestión de Indexadores']"
    xpath_button_crear_index = "//button[text()='Crear indexador']"
    xpath_button_origenes = "//button[text()='Origenes']"
    xpath_button_destinos = "//button[text()='Destinos']"
    xpath_button_index_data = "//div[@class='sc-kMzELR enAosP']"
    xpath_box_data_index = "//div[@class='sc-eAKtBH djJGJI']"
    xpath_index_list = "//div[@class='sc-fLseNd hqXmnK']"
    xpath_button_editar = "//a[@class='sc-hhyKGa eoyvXd']"


    class Post_Put():
        xpath_button_origen = "//button[text()='Origen']"
        xpath_button_destino = "//button[text()='Destino']"
        xpath_button_area = "//button[text()='Area']"
        xpath_input_descripcion = "//input[@placeholder='Descripción']"
        xpath_button_analizar_entidades = "//button[@class='sc-ftxyOh gjbsaY']"
        xpath_opcion_origen_de_datos = "//text[text()='Origen de Datos B']"
        xpath_opcion_destinos_de_datos = "//text[text()='Destino de Datos']"
        xpath_opcion_area_finanzas = "//text[text()='Finanzas']"
        xpath_opcion_area_administracion = "//text[text()='Administración]"
        xpath_button_confirmar = "//button[text()='Confirmar']"
        xpath_ventana_exito = "//div[@class='sc-cmfnrN ejoJGS']/button"
        

        


    class Origins():
        http = "http://localhost:5173/origins"

        #Xpaths
        xpath_title_orgines = "//text[text()='Origenes']"
        xpath_button_crear_origen = "//button[text()='Crear Origen']"
        xpath_tabla_origenes_desple = "//div[@class='sc-eAKtBH djJGJI']"
        xpath_box_data_origenes = "//div[@class='sc-kMzELR enAosP']"
        xpath_button_editar_origen = "//a[@class='sc-hhyKGa eoyvXd']"
        xpath_origenes_list = "//div[@class='sc-lnsjTu cfZiFe']"
        

        class Post_Put():
            xpath_button_seleccionar = "//button[text()='Tipo conector de datos']"
            xpath_opcion_microsoft_azure = "//text[text()='Microsoft Azure Blob Storage']"
            xpath_input_descripcion = "//input[@placeholder='Descripción']"
            xpath_input_BlobCNN = "//input[@placeholder='Blob CNN']"
            xpath_input_BlobContainer = "//input[@placeholder='Blob Container']"
            xpath_input_BlobFolder = "//input[@placeholder='Blob Folder']"
            xpath_button_confirmar = "//button[text()='Confirmar']"
            xpath_box_input = "//div[@class='sc-jIYCZY kynBZu']"
            xpath_ventana_exito = "//div[@class='sc-cmfnrN ejoJGS']/button"

    class Destinos():
        http = "http://localhost:5173/destinations"

        #Xpaths
        xpath_title_destinos = "//text[text()='Destinos']"
        xpath_button_crear_destinos = "//button[text()='Crear destino']"
        xpath_tabla_destinos_desple = "//div[@class='sc-jiaSqj lppLIT']"
        xpath_box_data_destinos = "//div[@class='sc-kZOsHZ fjajQX']"
        xpath_button_editar_destinos = "//a[@class='sc-eKzvBH DpQFV']" 
        xpath_destinos_list = "//div[@class='sc-BCDEK bcrdeb']"

        class Post_Put():
            xpath_button_seleccionar = "//button[text()='Tipo conector de datos']"
            xpath_opcion_microsoft_azure = "//text[text()='Microsoft Azure Blob Storage']"
            xpath_input_descripcion = "//input[@placeholder='Descripción']"
            xpath_input_BlobCNN = "//input[@placeholder='Blob CNN']"
            xpath_input_BlobContainer = "//input[@placeholder='Blob Container']"
            xpath_input_BlobFolder = "//input[@placeholder='Blob Folder']"
            xpath_button_confirmar = "//button[text()='Confirmar']"
            xpath_box_input = "//div[@class='sc-jIYCZY kynBZu']"
            xpath_ventana_exito = "//div[@class='sc-cmfnrN ejoJGS']/button"

class Areas():
    http = "http://localhost:5173/areas"

    #Xpath
    xpath_title_areas = "//text[text()='Areas']"
    xpath_button_crear_area = "//button[text()='Crear area']"
    xpath_finanzas_desplegable = "//div/text[text()='Finanzas']"
    xpath_administración_desplegable = "//div/text[text()='Administración']"
    xpath_box_data = "//div[@class='sc-eGgGjL htKqrE']"
    xpath_button_editar = "//a[@class='sc-lkDHyp HgCjD']"
    xpath_areas_list = "//div[@class='sc-YltrM bytqCq']"