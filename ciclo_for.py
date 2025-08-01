#Repetir una palabra 10 veces

word = input("Ingresa una palabra: ")

for i in range(10):
    print(word)

print("")

#Calcular cuadrado de un número de una lista

print("Comienzo")

print("")

contador = 1
for i in [3,4,5,6,7,8]:
    print(f'Vuelta número: {contador}')
    print(f'Hola, ahora i vale {i} y su cuadrado es {i ** 2}')
    print("")
    contador += 1
print("Final")

print("")

#Tabla de multiplicar

numero = int(input("¿De qué número quieres la tabla de multiplicar? "))
print("")

print(f'Tabla de multiplicar del número: {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i * numero}')