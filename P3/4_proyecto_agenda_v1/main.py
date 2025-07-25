import agenda

def main():

    opcion=True
    datos=[]

    while opcion:

        agenda.borrarPantalla()
        opcion=agenda.menu_principal()

        match opcion:
            case "1":
                agenda.agregarContacto(datos)
                agenda.esperarTecla()
            case "2":
                agenda.mostrarTodosLosContactos(datos)
                agenda.esperarTecla()
            case "3":
                agenda.buscarContactoPorNombre()
                agenda.esperarTecla()
            case "4":
                opcion=False
                agenda.borrarPantalla() 
                print("Terminaste la ejecucuion del SW")

            case _: 
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()