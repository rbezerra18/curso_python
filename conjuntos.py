"""
Conjuntos - Métodos
add // Añade un elemento al final del conjunto
pop // Devuelve y elimina un elemento arbitrario o devuelve un error si está vacío
remove // Elimina un elemento del conjunto, si no existe causa un error
union // Devuelve un conjunto con todos los elementos de ambos conjuntos
clear // Elimina toda la información del conjunto
"""

#1 forma de crear conjuntos
alumnos = {"Andrea", "Ruby", "Marcos", "Marlon", "Jose"}

print(type(alumnos))
print(alumnos)

#2 forma de crear conjuntos
lenguajes = set(["PHP", "Java", "C", "Python"])

print(type(lenguajes))
print(lenguajes)

lenguajes.add("C#")

print(lenguajes)

lenguajes.pop()

print(lenguajes)

lenguajes.remove("Java")

print(lenguajes)

todos = alumnos.union(lenguajes)

print(todos)

print(f"El conjunto todos contiene: {todos}")

todos.clear()

print(f"El conjunto todos está vacío: {todos}")