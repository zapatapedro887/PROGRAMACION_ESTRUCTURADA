ca=[]

def borraPantalla():
    import os
    os.system("cls")

ca.update("Escribie el nombre: ")
ca.input(float("escribe primer calificacion: "))
ca.input(float("Escribe segunda calificacion: "))
ca.input(float("Escribe tercer calificacion: "))

def agreagar_calificaciones():
    borraPantalla()
    print("\n\t.:: Alta de calificaciones ::\n")
    ca.update({"nombre":input("Ingrese el nombre: ").upper ().strip ()})
    ca.update({"calificacion 1":input("Ingrese la primera calificaion: ").upper ().strip ()})
    ca.update({"calificacion 2":input("Ingrese la segunda calificacion: ").upper ().strip ()})
    ca.update({"calificacion 3":input("Ingrese la tercera calificacion: ").upper ().strip ()})
    print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")



