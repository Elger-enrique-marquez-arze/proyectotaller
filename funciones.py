from conectar import conectar
from mysql.connector import Error

# Función para iniciar sesión
def iniciar_sesion(usuario, contrasena):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM cuentas WHERE usuario = %s AND password = %s"
            cursor.execute(query, (usuario, contrasena))
            cuenta = cursor.fetchone()
            if cuenta:
                print(f"Bienvenido {usuario}")
                return True  # Retorna True si la sesión es exitosa
            else:
                print("Usuario o contraseña incorrectos.")
                return False  # Retorna False si la sesión falla
        except Error as e:
            print(f"Error al iniciar sesión: {e}")
            return False  # En caso de error también retorna False
        finally:
            cursor.close()
            connection.close()

# CRUD para la tabla 'cuentas'
def agregar_cuenta(usuario, email, password, plataforma_id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO cuentas (usuario, email, password, plataforma_id, fecha_creacion) VALUES (%s, %s, %s, %s, NOW())"
            cursor.execute(query, (usuario, email, password, plataforma_id))
            connection.commit()
            print("Cuenta agregada correctamente.")
        except Error as e:
            print(f"Error al agregar cuenta: {e}")
        finally:
            cursor.close()
            connection.close()

def obtener_cuentas():
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM cuentas")
            cuentas = cursor.fetchall()
            for cuenta in cuentas:
                print(cuenta)
        except Error as e:
            print(f"Error al obtener cuentas: {e}")
        finally:
            cursor.close()
            connection.close()

def actualizar_cuenta(cuenta_id, usuario, email, password, plataforma_id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE cuentas SET usuario = %s, email = %s, password = %s, plataforma_id = %s WHERE id = %s"
            cursor.execute(query, (usuario, email, password, plataforma_id, cuenta_id))
            connection.commit()
            print("Cuenta actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar cuenta: {e}")
        finally:
            cursor.close()
            connection.close()

def eliminar_cuenta(cuenta_id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM cuentas WHERE id = %s"
            cursor.execute(query, (cuenta_id,))
            connection.commit()
            print("Cuenta eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar cuenta: {e}")
        finally:
            cursor.close()
            connection.close()

# CRUD para la tabla 'estadisticas_armas'
def agregar_estadistica_arma(cuenta_id, arma_id, tiempo_usado, kills, muertes):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO estadisticas_armas (cuenta_id, arma_id, tiempo_usado, kills, muertes) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (cuenta_id, arma_id, tiempo_usado, kills, muertes))
            connection.commit()
            print("Estadística de arma agregada correctamente.")
        except Error as e:
            print(f"Error al agregar estadística de arma: {e}")
        finally:
            cursor.close()
            connection.close()

def obtener_estadisticas_arma():
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM estadisticas_armas")
            estadisticas = cursor.fetchall()
            for estadistica in estadisticas:
                print(estadistica)
        except Error as e:
            print(f"Error al obtener estadísticas de armas: {e}")
        finally:
            cursor.close()
            connection.close()

def actualizar_estadistica_arma(id, cuenta_id, arma_id, tiempo_usado, kills, muertes):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE estadisticas_armas SET cuenta_id = %s, arma_id = %s, tiempo_usado = %s, kills = %s, muertes = %s WHERE id = %s"
            cursor.execute(query, (cuenta_id, arma_id, tiempo_usado, kills, muertes, id))
            connection.commit()
            print("Estadística de arma actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar estadística de arma: {e}")
        finally:
            cursor.close()
            connection.close()

def eliminar_estadistica_arma(id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM estadisticas_armas WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("Estadística de arma eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar estadística de arma: {e}")
        finally:
            cursor.close()
            connection.close()

# CRUD para la tabla 'mapas'
def agregar_mapa(nombre, tipo, descripcion):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO mapas (nombre, tipo, descripcion) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, tipo, descripcion))
            connection.commit()
            print("Mapa agregado correctamente.")
        except Error as e:
            print(f"Error al agregar mapa: {e}")
        finally:
            cursor.close()
            connection.close()

def obtener_mapas():
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM mapas")
            mapas = cursor.fetchall()
            for mapa in mapas:
                print(mapa)
        except Error as e:
            print(f"Error al obtener mapas: {e}")
        finally:
            cursor.close()
            connection.close()

def actualizar_mapa(id, nombre, tipo, descripcion):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE mapas SET nombre = %s, tipo = %s, descripcion = %s WHERE id = %s"
            cursor.execute(query, (nombre, tipo, descripcion, id))
            connection.commit()
            print("Mapa actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar mapa: {e}")
        finally:
            cursor.close()
            connection.close()

def eliminar_mapa(id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM mapas WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("Mapa eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar mapa: {e}")
        finally:
            cursor.close()
            connection.close()

# CRUD para la tabla 'membresias_clan'
def agregar_membresia_clan(cuenta_id, clan_id, rol):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO membresias_clan (cuenta_id, clan_id, rol) VALUES (%s, %s, %s)"
            cursor.execute(query, (cuenta_id, clan_id, rol))
            connection.commit()
            print("Membresía agregada correctamente.")
        except Error as e:
            print(f"Error al agregar membresía de clan: {e}")
        finally:
            cursor.close()
            connection.close()

def obtener_membresias_clan():
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM membresias_clan")
            membresias = cursor.fetchall()
            for membresia in membresias:
                print(membresia)
        except Error as e:
            print(f"Error al obtener membresías de clan: {e}")
        finally:
            cursor.close()
            connection.close()

def actualizar_membresia_clan(id, cuenta_id, clan_id, rol):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE membresias_clan SET cuenta_id = %s, clan_id = %s, rol = %s WHERE id = %s"
            cursor.execute(query, (cuenta_id, clan_id, rol, id))
            connection.commit()
            print("Membresía de clan actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar membresía de clan: {e}")
        finally:
            cursor.close()
            connection.close()

def eliminar_membresia_clan(id):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM membresias_clan WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print("Membresía de clan eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar membresía de clan: {e}")
        finally:
            cursor.close()
            connection.close()
