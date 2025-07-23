

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_principal():
    print("\n\t📓..::: agenda :::...📓 \n📓..::: Sistema de agenda :::...📓\n 1️⃣ agregar contacto  \n  2️⃣ mostrar todos los contacots \n  3️⃣ Buscar contacto por nombre \n 4️⃣ SALIR")
    opcion=input("\n\t\t Elige una opcion (1-4): ").upper()
    return opcion

def agregarContacto(datos):
    """Pide al usuario los datos del contacto y lo agrega a la lista."""
    print("Agregar nuevo contacto")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    datos.append(contacto)
    print(f"\nContacto {nombre} agregado con éxito.")

def mostrarTodosLosContactos(datos):
    """Muestra todos los contactos almacenados."""
    print("Lista de contactos:\n")
    if len(datos) == 0:
        print("No hay contactos registrados.")
        return
    for i, contacto in enumerate(datos, start=1):
        print(f"{i}. {contacto['nombre']} - Tel: {contacto['telefono']} - Email: {contacto['email']}")

def buscarContactoPorNombre(datos):
    """Busca y muestra contactos que coincidan con el nombre ingresado."""
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()
    encontrados = [c for c in datos if nombre_buscar in c['nombre'].lower()]
    
    if not encontrados:
        print(f"No se encontraron contactos con el nombre '{nombre_buscar}'.")
        return
    
    print(f"Resultados para '{nombre_buscar}':")
    for i, contacto in enumerate(encontrados, start=1):
        print(f"{i}. {contacto['nombre']} - Tel: {contacto['telefono']} - Email: {contacto['email']}")
