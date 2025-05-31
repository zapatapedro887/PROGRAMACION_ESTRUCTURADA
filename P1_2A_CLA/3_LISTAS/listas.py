import os
os.system("clear")

#ejemplo 2 crear una lista de numeros e imprimir el contenido
numeros=[1,2,3,4,5,6,7,8,9,10]

#1er forma
print(numeros)

# 2da forma- tabaja con el valor
for i in numeros:
    print(i)

#3er forma - trabaja con los indices
for i in range(0,len(numeros)):
    print(numeros[i])

#Ejemplo 2 crea una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=["ayer","nose","aveces","nose","confundido"]
print(palabras.count("nose"))

palabras_buscar=input("dame la palabra de buscar")

#1er forma
if palabras_buscar in palabras:
    print("se encontro la palabra")
else:
    print("no encontro la palabra")

# 2da forma
for i in palabras:
    if i==palabras_buscar:
        print("se encontro la palabra")
    else:
        print("no se encontro la palabra")

#3er forma
encontro=False
for i in palabras:
    if i==palabras_buscar:
        encontro=True

#4ta forma
if encontro:
    print("se encontro la palabra")
else:
    print("no encontro la palabra")

# 5ta fomra
# encontro=False
# for i in range(0,len(numeros)):
#     if palabras[i]==palabras_buscar:
#         encontro=True

#ejemplo3 añadir elementos a una lista
numeros=[]        
opc="si"
while opc=="si":
    numero=float(input("dame un numero entero o decimal: "))
    numeros.append(numero)
    opc=input("deseas solicitar otro numero? (si/no): ").lower()
print(numeros)

# 2da forma
numeros=[]        
opc="si"
while opc=="si":
    numeros.append(float(input("dame un numero entero o decimal: ")))
    opc=input("deseas solicitar otro numero? (si/no): ").lower()
print(numeros)

#crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas
personas = []

opc = "si"
while opc == "si":
    nombre = input("Dame un nombre: ")
    telefono = input("Dame un número de teléfono: ")
    personas.append([nombre, telefono]) 
    opc = input("¿Deseas ingresar otra persona? (si/no): ").lower()

print("\nLista de personas:")
for persona in personas:
    print("Nombre:", persona[0], "- Teléfono:", persona[1])


agenda=[
    ["carlos","635734756"]
    ["alberto","77568765"]
    ["martin","356458768"]
]

print(agenda)
for r in agenda:
    print(r)


for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

for r in range(0,3):
    for c in range (0,2):
        print(agenda[r][c])
print(agenda.count())



