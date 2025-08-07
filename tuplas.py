"""
Crear una tupla con números, luego pedir un número por teclado e:
- indicar cuantas veces se repite
- indicar cuál es la posición en la tupla
"""

numeros = (5,6,7,8,5,5,6,90,12,14,12)

numero = int(input("Dame un número: "))

print("El número se repite: " + str(numeros.count(numero)) + " veces.")

print("El número " + str(numero) + " se encuentra en el índice: " + str(numeros.index(numero)))