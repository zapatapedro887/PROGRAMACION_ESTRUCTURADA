#proyecto 1
#crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar,
#eliminar, modificar y consultar peliculas

#notas:
#1-. utlizar funciones y mandar llamar desdee otro archivo
#2-. utilizar, modificar y consultar peliculas


import peliculas

opcion=True
while opcion:
    peliculas.borrapantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- crear  \n 2.- borrar \n 3.- mostrar \n 4.- agregar caracteristicas \n 5.- modificar caracteristicas \n 6.- borrar caracteristicas \n 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearpeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarpeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agreagarCaracteristicaPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False  
            peliculas.borrapantalla()  
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

