
# Lista para guardar [nombre, teléfono]
personas = []

# Solo pedirá datos de 4 personas
for i in range(4):
    print(f"\nPersona {i+1}")
    nombre = input("Dame un nombre: ")
    telefono = input("Dame un número de teléfono: ")
    personas.append([nombre, telefono])

# Mostrar resultados
print("\nLista de personas:")
for persona in personas:
    print("Nombre:", persona[0], "- Teléfono:", persona[1])
