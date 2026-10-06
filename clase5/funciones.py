
# estructura básica de función 
suma = 20
def sumar(a=3, b=6):
    suma = a+b
    return suma
print(suma)
# invocando a la funciones 
print(sumar(40, 5))
# declando en una variable
resultado = sumar(30, 40)
print(resultado)

# funciones con valores por 
# defecto de los parametros
def saludar(apellido="espinoza",  nombre="pedrito"):
    print(f"hola {nombre} {apellido} ")

saludar("Espinoza", "Emerson")
saludar("Josue")
saludar("Jennifer")
saludar("Yerson")
saludar("suarez", "juan")
def cantidad(nombre):
    return nombre

print(len("emerson"))

# multiplica el resultado de una suma por 10 
def multiplicar(dato):
    resultado = sumar(50, 5)* dato
    return resultado
# para que el resultado de la multiplicación 
# se divida por un número
def division(dato):
    resultado = multiplicar(10)/ dato
    return resultado


print(multiplicar(10))
print(division(10))


# funciones que se llaman asi misma
def cuenta(n):
    if n == 0:
        return cuenta(n-1)
    else:
        return n

print(cuenta(10))
print(cuenta(0))

# calcular el area de un triangulo
# area = (base x altura)/2
