#proyecto 1
#crear un proyecto que permita gestionar (administrar) calificaciones, 
#colocar un menu de opciones para agregar,
#mostrar y calcular promedios de las calificaciones de los alumnos

#notas:
#1-. utlizar funciones y mandar llamar desdee otro archivo
#2-. utilizar listas para almacenar el nombre de un alumno y 3calificaciones


import calificaciones

def main():

    opcion=True
    datos=[]

    while opcion:

        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios()
                calificaciones.esperarTecla()
            case "4":
                opcion=False
                calificaciones.borrarPantalla() 
                print("Terminaste la ejecucuion del SW")

            case _: 
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()




