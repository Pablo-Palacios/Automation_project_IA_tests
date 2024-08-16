# README - Proyecto de Automatización de Tests para Ia_search

## Descripción del Proyecto

Este proyecto está enfocado en la automatización de pruebas para la API de `Ia_search`, una solución basada en inteligencia artificial para la búsqueda avanzada de datos. El objetivo principal es garantizar la estabilidad y robustez del sistema a través de pruebas exhaustivas en ambos extremos del sistema: backend y frontend.

### Pruebas en Backend

Las pruebas automatizadas del backend se centran en verificar los endpoints expuestos por la API, asegurando su correcto funcionamiento, validez de las respuestas y manejo adecuado de errores. Además de las pruebas funcionales típicas, se implementan también pruebas orientadas a romper el sistema, sometiendo a los endpoints a ataques comunes como inyecciones de código, entradas maliciosas y pruebas de carga.

### Pruebas en Frontend

Por otro lado, las pruebas en el frontend se ejecutan utilizando Selenium para emular la interacción de los usuarios con la aplicación web. Estas pruebas están diseñadas para validar la integridad de los elementos de la interfaz de usuario, así como las acciones que un usuario podría realizar, asegurando que todas las funcionalidades sean accesibles y respondan de manera adecuada a las interacciones del usuario.

## Requisitos Previos

- **Python**: Versiones recomendadas 3.10.0 >= 3.11.9
- **Selenium**: Para las pruebas del frontend.
- **pytest**: Marco de pruebas para ejecutar las pruebas.
- **otros**: Redis, locust, python-dotenv, faker, psycopg2, pickle5, unittest.

## Configuración del Proyecto

### 1. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto.

```shell
python3 -m venv venv
