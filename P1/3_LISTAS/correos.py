#crea un programa que solicite los emails de los alumnos de la utd alacenar 
#en un alista y posteriormente mostrar em pantalla los emails sin duplicados

email = []

opcion = "si"
while opcion == "si":
    email.append(input("Dame tu correo: ")) 
    opcion = input("¿Deseas ingresar otro correo? (si/no): ").lower()

# print(email)

#primero convierto mi lsita a set para eliminiar duplicados
email_set=set(email)
# print(email_set)

# despues conveirto denuevo el set a lsita

email=list(email_set)
print(email)