import mysql.connector

def conectar():
    try:
        # Establecer la conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Tu contraseña si la tienes
            database="videojuego"  # Nombre de tu base de datos
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None