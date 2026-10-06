
# listas en python
frutas = ["uva", "platano", "manzana" ]
copia_fruta = frutas.copy()
# mostrar un dato de la lista
print(frutas[1])
# print(frutas[3])
# modificar datos de la lista
frutas[0] = "naranja"
print(frutas)
# CRUD - CREATE - READ - UPDATE - DELETE
# crear un nuevo dato a la lista 
frutas.append("papaya")
print(frutas)

# para eliminar un dato
frutas.pop(2)
print(frutas)

# agregar muchos datos 
frutas.extend(["zapote", "fresa", "mango"])
print(frutas)
# agregar e insertar un dato en base a un indice 
frutas.insert(0, "chirimoya" )
print(frutas)
# para eliminar en base a su nombre del dato
frutas.remove("zapote")
print(frutas)

# para limpiar la lista 
# frutas.clear()
# print(frutas)
# para mostrar en base a su indice
buscador = frutas.index("mango")
print(buscador)
frutas.extend(["mango", "fresa", "fresa"])
print(frutas)
# contador de datos que se repite
contador = frutas.count("fresa")
print(contador)

# orden ascendente 
frutas.sort()
print(frutas)

numeros = [40, 1, 3, 20, 5, 4]
numeros.sort()
print(numeros)
# orden descendente 
frutas.sort(reverse=True)
print(frutas)

# para revertir una lista

datos = [4, 6, 1, 3, 30, 5]
datos.reverse()
print(datos)

# mostrar los datos originales 
print(copia_fruta)

ventas = [2000, 4000, 1000, 500, 5000]

venta_maxima = max(ventas)
print(f"la venta máxima fue: {venta_maxima} ")
venta_minima = min(ventas)
print(venta_minima)
cantida_ventas = len(ventas)
print(cantida_ventas)
venta_total = sum(ventas)
print(venta_total)

# para recorrer una lista
print(frutas)
for mensaje in frutas:
    print(f"bienvenido mi estimado: {mensaje} ")

matriz = [
    [1,5,7],
    [4,6,1],
    [5,4,6]
]
# mostrar
print(matriz[1][1])
print(matriz[2][1])

conjutos = [2, 3,3, 6, 6, 4]
print(conjutos)
print(set(conjutos))