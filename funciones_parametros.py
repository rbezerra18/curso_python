#Verficiar se un número es par o impar

def es_par(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

es_par(5)
es_par(10)

print("")

#Saludar una persona 

def saludar(nombre):
    print(f"Hola, {nombre} eres el mejor programador.")

saludar("Roberto")

print("")

#Hacer una resta entre dos números

def resta(a = None, b = None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función.")
        return
    return a - b

resta()

resultado = resta(5,2)
print(resultado)

print("")

#Hacer la tabla de multiplicación de un número

def multiplicacion(numero = None):
    if numero is None:
        print("Por favor, introduce un número.")
    else:
        print(f"TABLA DE MULTIPLICAR DEL {numero}")
        for i in range(1,11):
            print(f"{i} x {numero} = {i * numero}")

multiplicacion()

print("")

multiplicacion(4)

print("")

multiplicacion(8)