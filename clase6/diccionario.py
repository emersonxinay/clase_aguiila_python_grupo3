
persona = {
    "nombre":"Emerson",
    "ciudad": "Lima",
    "país": "Perú",
    "contraseña": "123456"
}
# CRUD con diccionarios
print(persona)
# mostrar el valor de una clave
print(persona["nombre"])
print(persona["contraseña"])

# agregar datos al diccionario
persona["edad"] = 20
print(persona)

# modificar un dato del diccionario
ciudad = input("ingrese su ciudad: ")
persona["ciudad"] = ciudad
print(persona)

# eliminar un dato en diccionario
del persona["contraseña"]
print(persona)
# para    que te avise que se elimino
eliminar = persona.pop("edad")
print(eliminar)
print(persona)

# recorrer un diccionario
# mostrar solo las claves
for x in persona:
    print(x)

for x in persona.keys():
    print(x)

# valor de las claves
for x in persona.values():
    print(x)

# para mostrar clave y valor
for x, y in persona.items():
    print(f"{x} - {y}")



# para saber si una clave existe o no 
dato = input("ingrese la clave a buscar: ")
buscador = persona.get(dato, "No existe")
print(buscador)

