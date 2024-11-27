from funciones import (
    iniciar_sesion,
    agregar_cuenta,
    obtener_cuentas,
    actualizar_cuenta,
    eliminar_cuenta,
    agregar_estadistica_arma,
    obtener_estadisticas_arma,
    actualizar_estadistica_arma,
    eliminar_estadistica_arma,
    agregar_mapa,
    obtener_mapas,
    actualizar_mapa,
    eliminar_mapa,
    agregar_membresia_clan,
    obtener_membresias_clan,
    actualizar_membresia_clan,
    eliminar_membresia_clan
)

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Iniciar sesión")
    print("2. Gestión de cuentas (CRUD)")
    print("3. Gestión de estadísticas de armas (CRUD)")
    print("4. Gestión de mapas (CRUD)")
    print("5. Gestión de membresías de clan (CRUD)")
    print("6. Salir")

def gestionar_cuentas():
    print("\n--- Gestión de Cuentas ---")
    print("1. Agregar cuenta")
    print("2. Obtener cuentas")
    print("3. Actualizar cuenta")
    print("4. Eliminar cuenta")
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        usuario = input("Ingrese el nombre de usuario: ")
        email = input("Ingrese el email: ")
        password = input("Ingrese la contraseña: ")
        plataforma_id = int(input("Ingrese el ID de la plataforma: "))
        agregar_cuenta(usuario, email, password, plataforma_id)
    elif opcion == '2':
        obtener_cuentas()
    elif opcion == '3':
        cuenta_id = int(input("Ingrese el ID de la cuenta a actualizar: "))
        usuario = input("Nuevo nombre de usuario: ")
        email = input("Nuevo email: ")
        password = input("Nueva contraseña: ")
        plataforma_id = int(input("Nuevo ID de plataforma: "))
        actualizar_cuenta(cuenta_id, usuario, email, password, plataforma_id)
    elif opcion == '4':
        cuenta_id = int(input("Ingrese el ID de la cuenta a eliminar: "))
        eliminar_cuenta(cuenta_id)

def gestionar_estadisticas_armas():
    print("\n--- Gestión de Estadísticas de Armas ---")
    print("1. Agregar estadística de arma")
    print("2. Obtener estadísticas de armas")
    print("3. Actualizar estadística de arma")
    print("4. Eliminar estadística de arma")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        cuenta_id = int(input("Ingrese el ID de la cuenta: "))
        arma_id = int(input("Ingrese el ID del arma: "))
        tiempo_usado = float(input("Ingrese el tiempo usado en horas: "))
        kills = int(input("Ingrese el número de kills: "))
        muertes = int(input("Ingrese el número de muertes: "))
        agregar_estadistica_arma(cuenta_id, arma_id, tiempo_usado, kills, muertes)
    elif opcion == '2':
        obtener_estadisticas_arma()
    elif opcion == '3':
        id = int(input("Ingrese el ID de la estadística a actualizar: "))
        cuenta_id = int(input("Nuevo ID de cuenta: "))
        arma_id = int(input("Nuevo ID de arma: "))
        tiempo_usado = float(input("Nuevo tiempo usado en horas: "))
        kills = int(input("Nuevo número de kills: "))
        muertes = int(input("Nuevo número de muertes: "))
        actualizar_estadistica_arma(id, cuenta_id, arma_id, tiempo_usado, kills, muertes)
    elif opcion == '4':
        id = int(input("Ingrese el ID de la estadística a eliminar: "))
        eliminar_estadistica_arma(id)

def gestionar_mapas():
    print("\n--- Gestión de Mapas ---")
    print("1. Agregar mapa")
    print("2. Obtener mapas")
    print("3. Actualizar mapa")
    print("4. Eliminar mapa")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del mapa: ")
        tipo = input("Ingrese el tipo de mapa: ")
        descripcion = input("Ingrese la descripción del mapa: ")
        agregar_mapa(nombre, tipo, descripcion)
    elif opcion == '2':
        obtener_mapas()
    elif opcion == '3':
        id = int(input("Ingrese el ID del mapa a actualizar: "))
        nombre = input("Nuevo nombre del mapa: ")
        tipo = input("Nuevo tipo de mapa: ")
        descripcion = input("Nueva descripción del mapa: ")
        actualizar_mapa(id, nombre, tipo, descripcion)
    elif opcion == '4':
        id = int(input("Ingrese el ID del mapa a eliminar: "))
        eliminar_mapa(id)

def gestionar_membresias_clan():
    print("\n--- Gestión de Membresías de Clan ---")
    print("1. Agregar membresía")
    print("2. Obtener membresías")
    print("3. Actualizar membresía")
    print("4. Eliminar membresía")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        cuenta_id = int(input("Ingrese el ID de la cuenta: "))
        clan_id = int(input("Ingrese el ID del clan: "))
        rol = input("Ingrese el rol en el clan: ")
        agregar_membresia_clan(cuenta_id, clan_id, rol)
    elif opcion == '2':
        obtener_membresias_clan()
    elif opcion == '3':
        id = int(input("Ingrese el ID de la membresía a actualizar: "))
        cuenta_id = int(input("Nuevo ID de cuenta: "))
        clan_id = int(input("Nuevo ID de clan: "))
        rol = input("Nuevo rol en el clan: ")
        actualizar_membresia_clan(id, cuenta_id, clan_id, rol)
    elif opcion == '4':
        id = int(input("Ingrese el ID de la membresía a eliminar: "))
        eliminar_membresia_clan(id)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if iniciar_sesion(usuario, contrasena):
                print("Sesión iniciada con éxito.")
            else:
                print("Error en el inicio de sesión.")
        elif opcion == '2':
            gestionar_cuentas()
        elif opcion == '3':
            gestionar_estadisticas_armas()
        elif opcion == '4':
            gestionar_mapas()
        elif opcion == '5':
            gestionar_membresias_clan()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()
