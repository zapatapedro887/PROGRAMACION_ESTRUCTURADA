#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

#pelicula=¨{
#      "nombre",
#      "categoria":"",
#     "clasificacion":"",
#        "genero":"",
#        "idioma":""
#}

pelicula={}


def borrapantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")
    
def crearpeliculas():
    borrapantalla()
    print("\n\t.:: Alta de Películas ::\n")
    pelicula.update({"nombre":input("Ingrese el nombre: ").upper ().strip ()})
    pelicula.update({"categoria":input("Ingrese la categoria: ").upper ().strip ()})
    pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper ().strip ()})
    pelicula.update({"genero":input("Ingrese el genero: ").upper ().strip ()})
    pelicula.update({"idioma":input("Ingrese el idioma: ").upper ().strip ()})
    print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():
    borrapantalla()
    print("\n\t.:: Consultar la  Película ::\n")
    if len(pelicula) > 0:
       for i in pelicula:
           print(f"\t{i}: {pelicula[i]}")
    else:
       print("\t.::No hay películas en el sistema.")

def borrarpeliculas():
     borrapantalla()
     print("\n\t.:: Borrar o quitar TODAS las  Películas ::\n")
     resp=input("¿Desas quitar o borrar todas las películas del sistema? (si/No): ")
     if resp== "si":   
      pelicula.cls()
      print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")  

def agreagarCaracteristicaPeliculas():
   borrapantalla()
   print("\n\t.:: Agregar Característicaa a  Películas ::\n")
   atributo= input("Ingrese la nueva característica de la película: ").lower() .strip()
   valor=input(f"Ingrese el valor de la característica de la pelicula: ").upper().strip()
   pelicula.update({atributo: input(f"Ingrese el valor de la característica '{atributo}': ").upper().strip()})
   pelicula[atributo] = valor
   print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n") 

def modificarCaracteristicaPeliculas():
   borrapantalla()
   print("\n\t.:: Modificar Características a Películas  ::. \n")
   if len(pelicula)>0:
    print(f"\n\tValor actuales: \n ")
    for i in pelicula:
      print(f"\t {(i)} : {pelicula[i]}")
      resp=input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
      if resp=="si":
        pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
   else:
     print("\t..:: No hay peliculas en Sistema  ::..")
     esperarTecla()


# def borrarCaracteristicaPeliculas():
#     borraPantalla()
#     print("\n\t.:: Borrar Características de la  Película ::\n")
#     atributo = input("Ingrese el nombre de la característica a borrar: ").lower().strip()
#     if atributo in pelicula:
#         del pelicula[atributo]
#         print(f"\n\t.::¡La característica '{atributo}' se ha borrado con éxito!::.\n")
#     else:
#         print(f"\n\t.::¡La característica '{atributo}' no existe en la película!::.\n")
#     print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n")

# def borrarCaracteristicaPeliculas(pelicula):
#     try:
#         borraPantalla()
#         print("\n\t.:: Borrar Características de la Película ::\n")
#         atributo = input("Ingrese el nombre de la característica a borrar: ").lower().strip()  
#         if atributo in pelicula:
#             del pelicula[atributo]
#             print(f"\n\t.:: ¡La característica '{atributo}' se ha borrado con éxito! ::.\n")
#             print("\n\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.\n")
#         else:
#             print(f"\n\t.:: ¡La característica '{atributo}' no existe en la película! ::.\n")
#     except Exception as e:
#         print("\n\t.:: ¡Ocurrió un error inesperado! ::.")
#         print(f"\tDetalle del error: {e}")

def borrarCaracteristicaPeliculas():
    borrapantalla()
    print("\n\t.:: Borrar Características de la Película ::\n")
    atributo = input("Ingrese el nombre de la característica a borrar: ").lower().strip()  
    if atributo in pelicula:
        del pelicula[atributo]
        print(f"\n\t.:: ¡La característica '{atributo}' se ha borrado con éxito! ::.\n")
        print("\n\t.:: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::.\n")
    else:
        print(f"\n\t.:: ¡La característica '{atributo}' no existe en la película! ::.\n")