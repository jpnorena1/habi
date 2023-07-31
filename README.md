Proyecto de Consulta de Inmuebles - Habi
Este proyecto es una herramienta que permite a los usuarios consultar los inmuebles disponibles para la venta. Los usuarios pueden filtrar los inmuebles por diferentes criterios, como año de construcción, ciudad y estado. Además, los usuarios pueden darle "me gusta" a los inmuebles para tener un ranking interno de los inmuebles más populares.

Requerimientos
Para ejecutar este proyecto, necesitarás tener instalado lo siguiente:

Python 3.7 o superior
Flask
MySQL Connector/Python
python-dotenv (para cargar las variables de entorno desde el archivo .env)
pytest (opcional, para ejecutar pruebas unitarias)
Configuración:

Clona el repositorio desde GitHub.
git clone https://github.com/tu_usuario/tu_proyecto.git


Crea un archivo .env en la raíz del proyecto y configura las variables de entorno:

DB_HOST=3.138.156.32
DB_USER=pruebas
DB_PASSWORD=VGbt3Day5R
DB_NAME=habi_db
PORT=3309

Instala las dependencias del proyecto.  
pip install -r requirements.txt

Estructura del Proyecto
La estructura del proyecto es la siguiente:

Estructura del Proyecto
La estructura del proyecto es la siguiente:

- app.py
- db_utils.py
- controllers/
  - consulta_controller.py
- models/
  - inmueble.py
- tests/
  - test_app.py
- requirements.txt
- .env

*app.py: Archivo principal que inicializa la aplicación Flask y registra los controladores.

*db_utils.py: Módulo que contiene la función para realizar consultas a la base de datos.

*controllers/consulta_controller.py: Módulo que define las rutas para el servicio de consulta de inmuebles.

*models/inmueble.py: Módulo que contiene la lógica de consulta de inmuebles utilizando el modelo.

*tests/test_app.py: Archivo que contiene las pruebas unitarias del proyecto.

*requirements.txt: Archivo que lista todas las dependencias del proyecto.

*.env: Archivo que contiene las variables de entorno para la configuración de la base de datos.

Uso
Para ejecutar el proyecto, simplemente ejecuta el archivo app.py:
python app.py
El servidor se iniciará y podrás acceder a las rutas desde tu navegador o mediante herramientas de consumo de APIs como Postman.

Contribuir
Si deseas contribuir a este proyecto, puedes hacerlo creando un fork y enviando tus pull requests. Asegúrate de seguir las guías de estilo y de escribir pruebas unitarias para las nuevas funcionalidades que agregues.

Licencia
Este proyecto está bajo la licencia MIT. Puedes consultar el archivo LICENSE para más detalles.

Contacto
Si tienes alguna pregunta o sugerencia sobre el proyecto, no dudes en contactarme.