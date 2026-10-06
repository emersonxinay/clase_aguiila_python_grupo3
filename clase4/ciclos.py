
# # ciclos con while 
# # de forma directa ciclo infinito
# while True:
#     print("Bienvenido al ciclo")

inicio = 0
while inicio < 5:
    print(f"conteo en: {inicio} ")
    inicio = inicio + 1

correo = input("Correo: ")
while correo != "emer@gmail.com":
    correo = input("Correo: ")

print("Correo válido")

# acumulador
contador = 1
suma = 0 
while contador <= 3:
    suma = suma + contador 
    contador = contador + 1

print(f"la suma total es: {suma}")

# ciclos con for y range
# rango con 1 solo argumento

for x in range(5):
    print(f"conteo en: {x}")

# rango con 2 argumentos 
for c in range(3, 10):
    print(f"conteo en {c} ")

# rango con 2 argumentos 
for c in range(0, 13):
    print(f" 5 x {c} = {c*5} ")

# rango con 3 argumentos 
for b in range(0, 10, 2 ):
    print(b)

# bucles anidados 
for k in range(0, 2 ):
    for w in range(0, 3) :
        print(w, k)
