import mysql.connector
import os
from dotenv import load_dotenv


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('PORT', 3306)  # Si PORT no está definido en el archivo .env, se usa el valor por defecto 3306
}

# Función para realizar consultas a la base de datos y obtener claves y valores
def execute_query(query, args=None):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if args:
        cursor.execute(query, args)
    else:
        cursor.execute(query)

    # Obtener nombres de columnas (claves)
    column_names = [col[0] for col in cursor.description]

    # Obtener valores de cada fila de resultados
    results = []
    for row in cursor.fetchall():
        row_data = {}
        for idx, value in enumerate(row):
            row_data[column_names[idx]] = value
        results.append(row_data)

    conn.commit()
    cursor.close()
    conn.close()
    return results
