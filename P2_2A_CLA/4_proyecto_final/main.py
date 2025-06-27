import funciones 
funciones.borra_pantalla()

def main():
    productos = []  # ["Gordita de chicharrón", 25.0]
    ventas = []     # [[producto, cantidad, total], ...]
    gastos = []     # [("gas", 300), ("masa", 200)]

    opcion = True
    while opcion:
        funciones.menu()
        opcion = input("\n\tSelecciona una opción: ").strip()  

        match opcion:
            case "1":
                funciones.registrar_producto(productos)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "2":
                funciones.actualizar_producto(productos)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "3":
                funciones.borrar_producto(productos)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "4":
                funciones.registrar_venta(productos, ventas)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "5":
                funciones.ver_ventas_totales(ventas, gastos)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "6":
                funciones.registrar_gasto(gastos)
                input("se realizo con exito precione cualquier tecla")
                funciones.borra_pantalla()
                
            case "7":
                print("\n\tCerrando programa... ¡Gracias por usar el sistema!")
                input("\n\tOprima una tecla para continuar")
                opcion = False  
            case _:
                print("\n\tOpción no válida. Intenta de nuevo.")
    
    print("\n\tGracias por usar el sistema. Hasta luego...")

if __name__ == "__main__":
    main()