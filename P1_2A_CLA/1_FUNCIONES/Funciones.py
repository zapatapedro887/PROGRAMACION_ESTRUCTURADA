#"""
  #Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  #Sintaxis:

   #def nombredeMifuncion(parametros):
      #bloque o conjunto de instrucciones

   #nombredeMifuncion(parametros)

   #Las funciones pueden ser de 4 tipos
  
    #Funciones de tipo "Procedimiento" 
   #1.- Funcion que no recibe parametros y no regresa valor
   #3.- Funcion que recibe parametros y no regresa valor
    
    #Funciones de tipo "Funcion"
   #2.- Funcion que no recibe parametros y regresa valor
   #4.- Funcion que recibe parametros y regresa valor

#""" 
#1-Funciones que no recibe paramtros y no regresa valor
def solicitarDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"Nombre: {nombre} y su telefono: {telefono}")
#2-Funciones que recibe paramtros y no regresa valor
def solicitarDatos3(nom,tel):
    nombre=nom
    telefono=tel
    print(f"Nombre: {nombre} y su telefono: {telefono}")
#3-Funciones que no recibe paramtros y regresa valor
def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return nombre,telefono
#4-Funciones que recibe paramtros y regresa valor
def solicitarDatos4(nom,tel):
    nombre=nom
    telefono=tel
    return nombre,telefono

#Mandar llamar o invocar las funciones

solicitarDatos1()

nombre=input("escribe el nombre")
telefono=input("escribe el telefono")
solicitarDatos3(nombre,telefono)

nom,tel=solicitarDatos2()
print(f"Los datos de la agenda son:")
