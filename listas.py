"""
Escribir un programa que almacene las asignaturas de un curso
"""

#Crea una variable con 4 índices [0, 1, 2, 3]
asignaturas = ["Matemáticas","Física","Español","Inglés"]

#Muestra el contenido de la variable en un determinado índice
print(asignaturas[0])
print(asignaturas[1])
print(asignaturas[2])
print(asignaturas[3])

print("")

#Muestra el tipo de la variable (List)
print(type(asignaturas))

print("")

#Loteria
numeros = []

for i in range(6):
    numeros.append(int(input("Introduce un número: ")))

numeros.sort()

print(f"Los números ganadores son: {numeros}")

print("")

#Imprimir lista
lista = [1,4,5,6,7,7,7,8,"Hola"]

#Excluir datos de la lista
lista.remove(7) #1. Remove por contenido de la variable
lista.pop(6) #2. Remove por índice de la lista
del lista[5] #3. Remove por índice de la lista

for i in lista:
    print(i)

print("")

#Limpiar la lista
lista.clear()
print("Esta es la lista después de colocar el método clear: " + str(lista))

print("")

#Contar número de veces que el contenido de la variable se repite
lista = [1,4,5,6,7,7,7,8,"Hola","Hola"]
print(lista)
print(f"El número 7 repite {lista.count(7)} veces.")
print(f"La palabra Hola repite {lista.count("Hola")} veces.")

print("")

#Descubrir en caul índice está el contenido de la variable
print(f"El número 8 está no índice {lista.index(8)}.")
print(f"La palabra Hola está no índice {lista.index("Hola")}.")

print("")

#Inverter el orden de la lista
lista.reverse()
print(lista)