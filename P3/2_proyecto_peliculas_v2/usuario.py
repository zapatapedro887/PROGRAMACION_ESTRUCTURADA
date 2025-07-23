import mysql Connector
from mysql connector error

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
    
def conectar():
   try:
      conexion = mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="",
         database="bd_peliculas"
      )
        return conexion
    except Error as e:
      print(f"el error que se presenta es: {e}" )
      return None

def crearpeliculas():
    borrapantalla()
    conexionBD!=conectar()
    if conexionBD! = None:
        print("\n\t.:: Alta de Películas ::\n")
        pelicula.update({"nombre":input("Ingrese el nombre: ").upper ().strip ()})
        pelicula.update({"categoria":input("Ingrese la categoria: ").upper ().strip ()})
        pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper ().strip ()})
        pelicula.update({"genero":input("Ingrese el genero: ").upper ().strip ()})
        pelicula.update({"idioma":input("Ingrese el idioma: ").upper ().strip ()})

        cursor=conexionBD.cursor
        sql="insert into peliculas ( nombre, categoria, clasificacion, genero, idioma) value (%s,%s,%s,%s,%s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        cursor.execute(sql,val)
        conexionBD.commit()

        print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():
    borrapantalla()
    conexion=conectar()
    if conexionBD!=None:
        print("\n\t.:: Consultar la  Película ::\n")
        cursor=conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        
        if registros:
           print("mostrar las peliculas")
           print(f"{"id": <10 }{"nombre": <15 }{"categoria": <15 }{"clasificacion": <15 }{"genero": <15 }{"idioma": <15 }")
           print(f"-"*80)
           for pelis in registros:
            print(f"{pelis[0]: <10}{pelis[1]: <15}{pelis[2]: <15}{pelis[3]: <15}{pelis[4]: <15}{pelis[5]: <15}")
            print(f"-"*80)
        else:
            print("\t.::No hay películas en el sistema.")

def buscarPeliculas():
    borrapantalla()
    conexion=conectar()
    if conexionBD!=None:
        print("\n\t.:: buscar la  Película ::\n")
        nombre=input("ingresa el nombre de la pelicula a buscar").upper
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        
        if registros:
           print("mostrar las peliculas")
           print(f"{"id": <10 }{"nombre": <15 }{"categoria": <15 }{"clasificacion": <15 }{"genero": <15 }{"idioma": <15 }")
           print(f"-"*80)
           for pelis in registros:
            print(f"{pelis[0]: <10}{pelis[1]: <15}{pelis[2]: <15}{pelis[3]: <15}{pelis[4]: <15}{pelis[5]: <15}")
            print(f"-"*80)
        else:
            print("\t.::película no encontrada en el sistema.")

def borrarPeliculas():
    borrapantalla()
    conexion=conectar()
    if conexionBD!=None:
        print("\n\t.:: buscar la  Película ::\n")
        nombre=input("ingresa el nombre de la pelicula a borrar").upper.strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        
        if registros:
           print("mostrar las peliculas")
           print(f"{"id": <10 }{"nombre": <15 }{"categoria": <15 }{"clasificacion": <15 }{"genero": <15 }{"idioma": <15 }")
           print(f"-"*80)
           for pelis in registros:
            print(f"{pelis[0]: <10}{pelis[1]: <15}{pelis[2]: <15}{pelis[3]: <15}{pelis[4]: <15}{pelis[5]: <15}")
            print(f"-"*80)
            resp=input(f"deseas borrar la pelicula{nombre}? (si/no): ").lower().strip()
            
        else:
            print("\t.::película no encontrada en el sistema.")

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

        