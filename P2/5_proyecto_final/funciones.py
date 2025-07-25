def borra_pantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print(
        "\n\t...::: GORDITAS :::..."
        "\n\t..::: Sistema de Gestión de Local :::..."
        "\n\t1.- Registrar producto"
        "\n\t2.- Actualizar producto"
        "\n\t3.- Borrar producto"
        "\n\t4.- Registrar venta"
        "\n\t5.- Ver ventas totales"
        "\n\t6.- Registrar gasto"
        "\n\t7.- SALIR"
    )


def registrar_producto(productos):
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        productos.append([nombre, precio])
        print("Producto registrado con éxito.")
    except ValueError:
        print("Precio inválido. Intenta de nuevo.")


def actualizar_producto(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    for i, prod in enumerate(productos):
        print(f"{i+1}. {prod[0]} - ${prod[1]}")
    try:
        idx = int(input("¿Qué producto quieres actualizar? (número): ")) - 1
        if 0 <= idx < len(productos):
            nuevo_precio = float(input("Nuevo precio: "))
            productos[idx][1] = nuevo_precio
            print("Producto actualizado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def borrar_producto(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    for i, prod in enumerate(productos):
        print(f"{i+1}. {prod[0]} - ${prod[1]}")
    try:
        idx = int(input("¿Qué producto quieres borrar? (número): ")) - 1
        if 0 <= idx < len(productos):
            productos.pop(idx)
            print("Producto borrado.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def registrar_venta(productos, ventas):
    if not productos:
        print("No hay productos registrados.")
        input("\nPresiona ENTER para continuar...")
        return

    print("\n--- PRODUCTOS DISPONIBLES ---")
    for i, prod in enumerate(productos):
        print(f"{i+1}. {prod[0]} - ${prod[1]:.2f}")

    try:
        idx = int(input("Selecciona el producto vendido (número): ")) - 1
        if 0 <= idx < len(productos):
            cantidad = int(input("¿Cuántas unidades?: "))
            total = productos[idx][1] * cantidad
            ventas.append([productos[idx][0], cantidad, total])
            print(f"\n✅ Total a pagar por el cliente: ${total:.2f}")
            input("\nPresiona ENTER para continuar...")
        else:
            print("Índice inválido.")
            input("\nPresiona ENTER para continuar...")
    except ValueError:
        print("Entrada inválida.")
        input("\nPresiona ENTER para continuar...")


def ver_ventas_totales(ventas, gastos):
    total_ventas = sum(v[2] for v in ventas)
    total_clientes = len(ventas)
    total_gastos = sum(g[1] for g in gastos)
    utilidad = total_ventas - total_gastos

    print(f"\nTotal de clientes: {total_clientes}")
    print(f"Ingresos por ventas: ${total_ventas:.2f}")
    print(f"Gastos del negocio: ${total_gastos:.2f}")
    print(f"Utilidad neta: ${utilidad:.2f}")


def registrar_gasto(gastos):
    descripcion = input("¿En qué fue el gasto?: ")
    try:
        monto = float(input("¿Cuánto se gastó?: "))
        gastos.append((descripcion, monto))
        print("Gasto registrado.")
    except ValueError:
        print("Monto inválido.")