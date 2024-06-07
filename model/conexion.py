import pymysql

def conexion ():
    
# Configuración de la conexión a la base de datos
    config = {
        'host': 'localhost',     # Cambia esto si tu servidor MariaDB está en otro host
        'user': 'benja',         # Usuario de la base de datos
        'password': 'Benja', # Contraseña del usuario
        'database': 'Universidad', # Nombre de la base de datos
    }
    
    # Conectar a la base de datos
    connection = pymysql.connect(**config)
    return connection

