#Calculadora de INDICE DE MASA CORPORAL (IMC)

print("Calculadora de INDICE DE MASA CORPORAL (IMC)\n")

contador = 0

while contador != 2:
    contador = int(input("¿Quieres seguir calculando el IMC?\n"
                         "1. Si\n"
                         "2. No\n"))

    print("")

    if contador == 1:
        estatura = float(input("Ingrese su estatura em metros: "))
        peso = float(input("Ingrese su peso em kilogramos: "))
        resultado = round(peso/(estatura**2), 2)

        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO\n')
        elif 18.5 < resultado < 24.99:
            print(f'IMC {resultado} = PESO NORMAL\n')
        elif 25 < resultado <= 30:
            print(f'IMC {resultado} = SOBREPESO\n')
        elif resultado > 30:
            print(f'IMC {resultado} = OBESIDAD\n')

    elif contador == 2:
        print("Hasta pronto!\n")

print("Gracias por usar la calculadora de IMC.")