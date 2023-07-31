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

MICROSERVICIO LIKE 

CREAMOS LA CONSULTA SQL


Para agregar la funcionalidad de "Me gusta" a la base de datos, necesitas realizar cambios en la estructura de las tablas y agregar una nueva tabla que registre los "me gusta" de los usuarios a los inmuebles. Aquí está la modificación que debes hacer en el esquema de la base de datos:
Agregar una nueva tabla "likes" para registrar los "me gusta":


CREATE TABLE IF NOT EXISTS `habi_db`.`likes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `property_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `likes_user_property_unique` (`user_id`, `property_id`) VISIBLE,
  INDEX `likes_user_id_fk` (`user_id` ASC) VISIBLE,
  INDEX `likes_property_id_fk` (`property_id` ASC) VISIBLE,
  CONSTRAINT `likes_user_id_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `habi_db`.`auth_user` (`id`),
  CONSTRAINT `likes_property_id_fk`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

Modificar la tabla "property" para agregar una nueva columna "likes_count" que registre la cantidad de "me gusta" que ha recibido cada inmueble:

ALTER TABLE `habi_db`.`property`
ADD COLUMN `likes_count` INT(11) NOT NULL DEFAULT 0;

Actualizar la lógica del servicio de "Me gusta" en el código:
En el código de tu servicio, Se debera agregar la lógica para registrar los "me gusta" de los usuarios a los inmuebles en la tabla "likes" y actualizar la columna "likes_count" en la tabla "property" cada vez que se da un "me gusta" a un inmueble.

________________________________SEGUNDO EJERCICIO_____________________________________
Para el segundo ejercicio, que es la manipulación del arreglo "myArray" y la impresión de las secuencias ordenadas, aquí hay un enfoque general sobre cómo abordarlo:

Tecnología a utilizar:

Lenguaje de programación: Python
Desarrollo del algoritmo para ordenar y separar los bloques del arreglo "myArray":

Recorrer el arreglo "myArray" y dividirlo en bloques utilizando el número cero como marcador de separación.
def ordenar_separar_bloces(myArray):
    resultado = []
    bloque_actual = []

    for num in myArray:
        if num == 0:
            if bloque_actual:
                resultado.append(''.join(sorted(map(str, bloque_actual))))
            else:
                resultado.append("X")
            bloque_actual = []
        else:
            bloque_actual.append(num)

    if bloque_actual:
        resultado.append(''.join(sorted(map(str, bloque_actual))))

    return ' '.join(resultado)

# Ejemplo de uso:
myArray = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
resultado = ordenar_separar_bloces(myArray)
print(resultado)  # Salida: "123 1378 167"

Para cada bloque, ordenar los números individualmente de menor a mayor.
Si un bloque no contiene elementos, reemplazarlo con "X".
Imprimir las secuencias separando los bloques por un espacio.
Ejemplo de implementación en Python:
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