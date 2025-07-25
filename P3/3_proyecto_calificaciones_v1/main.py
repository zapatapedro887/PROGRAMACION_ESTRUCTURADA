#proyecto 1
# Crear un proyecto que permita Gestionar (Administrar) películas, colocar un menú de opciones para agregar, eliminar, modificar y consultar películas.

#Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar dict para almacenar los siguientes atributos: (nombre, categoría,clasificacion,genero,idioma) de las peliculas#
# 3.- Utilizar e implementar una BD para gestionar las películas
#  
importar películas

opción=Verdadero
mientras opción:
    películas.borrarPantalla()
    imprimir("\norte\t\t\t..::: CLON DE CINEPOLIS :::...\norte\t\t..::: Sistema de Gestión de Películas :::...\norte\t\t\t1.- Crear  \norte\t\t\t2.- Borrar\norte\t\t\t3.- Mostrar\norte\t\t\t4.- Modificar  \norte\t\t\t5.- Buscar\norte\t\t\t6.- Salir")
    opción=aporte("\norte\t\t\tElige una opción: ").superior()

    fósforo opción:
        caso "1":
            películas.crearPelículas()
            películas.EsperarTecla()
        caso "2":
            películas.borrarPeliculas()
            películas.EsperarTecla()
        caso "3":
            películas.MostrarPelículas()
            películas.EsperarTecla()
        caso "4":
            películas.modificarPelículas()
            películas.EsperarTecla()
        caso "5":
            películas.buscarPelículas()
            películas.EsperarTecla()
        caso "6":
            opción=FALSO    
            películas.borrarPantalla()
            imprimir("\norte\tTerminaste la ejecucion del SW")    
        caso_:
            películas.borrarPantalla()
            aporte("\norte\tOpción invalida vuelva a intentarlo... por favor")

