#Uso de parámetros
def suma1(a, b, c):
    return a + b + c

resultado1 = suma1(3, 4, 5)

print(resultado1)

#Uso de args
def suma2(*args):
    s= 0
    for arg in args:
        s += arg
    return s

resultado2 = suma2(10, 10, 10, 20)

print(resultado2)

"""
#Uso de args
def lenguaje(nombre, *lenguajes):
    print(f"Hola, {nombre}.")
    print(f"Tus lenguajes favoritas son: {lenguajes}")

lenguaje("Roberto", "Ruby", "Python", "Java", "PHP")

"""

#Uso de kwargs
def lenguaje(nombre, **kwargs):
    print(f"Hola, {nombre}.")
    print("Información:")

    contador = 0

    for clave in kwargs:
        contador += 1
        print(f"Tu {contador} lenguaje favorito es {kwargs[clave]}")

lenguaje("Roberto", lenguaje1 = "Ruby", lenguaje2 = "Python", lenguaje3 = "Java", lenguaje4 = "PHP")