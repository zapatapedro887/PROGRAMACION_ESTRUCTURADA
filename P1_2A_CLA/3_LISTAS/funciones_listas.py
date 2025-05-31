"""
List (Array)
son colleciones o conjuntos de datos/valores bajo un mismo
nombre, para acceder a los valores se hace con un indice 
numerico

Nota:sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite
miembros duplicados

"""

import os
os.system("clear")

#funciones mas comunes en las listas
paises=["méxico","brasil","españa","canada"]

numeros=[23,12,100,34]

varios=["hola",True,33,3.12]

#Ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)

paises.sort()
print(paises)

#Agragar o insertar o añdir un elemento a la lista
#1er forma: paises=["méxico","brasil","españa","canada"]

print(paises)
paises.append("honduras")
print(paises)

#2da forma
paises.insert(1,"honduras")
print(paises)

#Eliminar o borrar o suprimir un elemento a la lista
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma
paises.remove("honduras")
print(paises)

# buscar un elemetno dentro de una lista
# paises=["méxico","brasil","españa","canada"]

print("brasil" in paises)

#contar el numero de veces que un elementos que esta dentro de una lista
# numeros=[23,12,100,34]
print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(12))

#dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(numeros)
print(paises)

#conocer pocicion de un dato de la lista 
print(paises.index("españa"))

# casmbiar un valor por otro
posision=paises.index("españa")
paises[posision]="ESPAÑA"
print (paises)

#unir el contenido de dos o mas listas en una sola
# numeros=[23,12,100,34]
numeros2=300,500,100

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)




