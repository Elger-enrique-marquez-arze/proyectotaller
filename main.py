from conectar import conectar
from mysql.connector import Error

def mostrar_menu():
    print("Bienvenido al menú de gestión.")
    print("1. Gestionar cuentas de usuario")
    print("2. Gestionar estadísticas de armas")
    print("3. Gestionar mapas")
    print("4. Gestionar membresías de clan")
    print("5. Salir")

def gestionar_cuentas():
    print("Gestión de cuentas de usuario:")
    print("1. Agregar cuenta")
    print("2. Obtener cuentas")
    print("3. Actualizar cuenta")
    print("4. Eliminar cuenta")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        usuario = input("Ingrese el usuario: ")
        email = input("Ingrese el email: ")
        password = input("Ingrese la contraseña: ")
        plataforma_id = input("Ingrese el ID de la plataforma: ")
        agregar_cuenta(usuario, email, password, plataforma_id)
    elif opcion == '2':
        obtener_cuentas()
    elif opcion == '3':
        cuenta_id = input("Ingrese el ID de la cuenta a actualizar: ")
        usuario = input("Ingrese el nuevo usuario: ")
        email = input("Ingrese el nuevo email: ")
        password = input("Ingrese la nueva contraseña: ")
        plataforma_id = input("Ingrese el nuevo ID de la plataforma: ")
        actualizar_cuenta(cuenta_id, usuario, email, password, plataforma_id)
    elif opcion == '4':
        cuenta_id = input("Ingrese el ID de la cuenta a eliminar: ")
        eliminar_cuenta(cuenta_id)
    else:
        print("Opción inválida.")

def gestionar_estadisticas_armas():
    print("Gestión de estadísticas de armas:")
    print("1. Agregar estadística")
    print("2. Obtener estadísticas")
    print("3. Actualizar estadística")
    print("4. Eliminar estadística")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        cuenta_id = input("Ingrese el ID de la cuenta: ")
        arma_id = input("Ingrese el ID del arma: ")
        tiempo_usado = input("Ingrese el tiempo usado: ")
        kills = input("Ingrese el número de kills: ")
        muertes = input("Ingrese el número de muertes: ")
        agregar_estadistica_arma(cuenta_id, arma_id, tiempo_usado, kills, muertes)
    elif opcion == '2':
        obtener_estadisticas_arma()
    elif opcion == '3':
        id = input("Ingrese el ID de la estadística a actualizar: ")
        cuenta_id = input("Ingrese el nuevo ID de la cuenta: ")
        arma_id = input("Ingrese el nuevo ID del arma: ")
        tiempo_usado = input("Ingrese el nuevo tiempo usado: ")
        kills = input("Ingrese el nuevo número de kills: ")
        muertes = input("Ingrese el nuevo número de muertes: ")
        actualizar_estadistica_arma(id, cuenta_id, arma_id, tiempo_usado, kills, muertes)
    elif opcion == '4':
        id = input("Ingrese el ID de la estadística a eliminar: ")
        eliminar_estadistica_arma(id)
    else:
        print("Opción inválida.")

def gestionar_mapas():
    print("Gestión de mapas:")
    print("1. Agregar mapa")
    print("2. Obtener mapas")
    print("3. Actualizar mapa")
    print("4. Eliminar mapa")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del mapa: ")
        tipo = input("Ingrese el tipo de mapa: ")
        descripcion = input("Ingrese la descripción del mapa: ")
        agregar_mapa(nombre, tipo, descripcion)
    elif opcion == '2':
        obtener_mapas()
    elif opcion == '3':
        id = input("Ingrese el ID del mapa a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del mapa: ")
        tipo = input("Ingrese el nuevo tipo de mapa: ")
        descripcion = input("Ingrese la nueva descripción del mapa: ")
        actualizar_mapa(id, nombre, tipo, descripcion)
    elif opcion == '4':
        id = input("Ingrese el ID del mapa a eliminar: ")
        eliminar_mapa(id)
    else:
        print("Opción inválida.")

def gestionar_membresias_clan():
    print("Gestión de membresías de clan:")
    print("1. Agregar membresía")
    print("2. Obtener membresías")
    print("3. Actualizar membresía")
    print("4. Eliminar membresía")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        cuenta_id = input("Ingrese el ID de la cuenta: ")
        clan_id = input("Ingrese el ID del clan: ")
        rol = input("Ingrese el rol de la cuenta en el clan: ")
        agregar_membresia_clan(cuenta_id, clan_id, rol)
    elif opcion == '2':
        obtener_membresias_clan()
    elif opcion == '3':
        id = input("Ingrese el ID de la membresía a actualizar: ")
        cuenta_id = input("Ingrese el nuevo ID de la cuenta: ")
        clan_id = input("Ingrese el nuevo ID del clan: ")
        rol = input("Ingrese el nuevo rol: ")
        actualizar_membresia_clan(id, cuenta_id, clan_id, rol)
    elif opcion == '4':
        id = input("Ingrese el ID de la membresía a eliminar: ")
        eliminar_membresia_clan(id)
    else:
        print("Opción inválida.")

def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_cuentas()
        elif opcion == '2':
            gestionar_estadisticas_armas()
        elif opcion == '3':
            gestionar_mapas()
        elif opcion == '4':
            gestionar_membresias_clan()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

def registrar_usuario():
    print("Registro de nuevo usuario:")
    usuario = input("Ingrese el usuario: ")
    email = input("Ingrese el email: ")
    password = input("Ingrese la contraseña: ")
    plataforma_id = input("Ingrese el ID de la plataforma: ")
    agregar_cuenta(usuario, email, password, plataforma_id)
    print("Usuario registrado exitosamente.")

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
                menu_principal()  # Accede al menú principal si el inicio de sesión es exitoso
            else:
                print("Usuario o contraseña incorrectos.")
        except Error as e:
            print(f"Error al iniciar sesión: {e}")
        finally:
            cursor.close()
            connection.close()

# Llamada al flujo de registro o inicio de sesión
def flujo_registro_o_inicio():
    print("Seleccione una opción:")
    print("1. Iniciar sesión")
    print("2. Registrar nuevo usuario")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        usuario = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        iniciar_sesion(usuario, contrasena)
    elif opcion == '2':
        registrar_usuario()
        usuario = input("Ingrese el usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        iniciar_sesion(usuario, contrasena)
    else:
        print("Opción inválida.")

# Llamada al flujo de inicio de sesión o registro
flujo_registro_o_inicio()
