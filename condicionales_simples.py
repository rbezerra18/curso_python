"""
Primer ejemplo:
Crear un programa que reciba el número de años que tiene nuestra computadora.
Imprimir en consola si es nuevo o es viejo.
Condiciones:
- Si es menor o igual a dos años, entonces es nuevo.
- Pero, se es mayor a dos anõs, entonces es viejo.
"""

anios = int(input("¿Cuántos años tiene tu computador?"))

if anios >= 0 and anios <= 2:
    print("Tu computador es nuevo.")
else:
    print("Tu computador es viejo.")

"""
Segundo ejemplo:
Crear un programa que reciba el número de años que tienes.
Imprimir en consola si es mayor o menor de edad.
Condiciones:
- Si es mayor o igual a dieciocho años, entonces es mayor.
- Pero, se es menor a dieciocho anõs, entonces es menor.
"""

edad = int(input("¿Cuántos años tienes?"))

if edad >= 18:
    print("Es usted mayor de edad.")
else:
    print("Es usted menor de edad.")

print("¡Hasta la próxima!")