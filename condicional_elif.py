"""
En una escuela de conducción se tiene un programa que dependiendo de la edad del
usuario debe mostrar el tipo de licencia a la que tiene derecho.
Condiciones:
    1. Si es menor a 16, entonces no puede conducir;
    2. Si es menor a 18, entonces puede obtener un permiso para conducir;
    3. Si es menor a 70, entonces puede obtener una licencia estándar;
    4. Si es mayor o igual a 70, entonces necesita una licencia especial.
"""

edad = int(input("Digita tu edad: "))

if edad < 16:
    print("No tienes edad para conducir.")
elif edad < 18:
    print("Puedes obtener un permiso para conducir.")
elif edad < 70:
    print("Puedes obtener una licencia estándar.")
else:
    print("Puedes obtener una licencia especial.")