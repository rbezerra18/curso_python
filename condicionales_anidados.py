"""
Pedir edad y graduación.
Condicionales:
- Si mayor o igual a 18, felicitar.
    - Si graduado, felicitar.
- No felicitar si menor a 18, aúnque sea graduado.
"""

edad = int(input("¿Cuántos años tienes? "))
graduacion = input("¿Ya te has graduado? (si) o (no) ")

if edad >= 18:
    print("¡Felicitaciones! Ya tienes la mayoría de edad.")

    if graduacion == 'si':
        print("¡Felicidades por tu graduación!")

"""
Pedir contraseña y verificar la cantidad de caracteres.
Condicionales:
- Si mayor o igual a 8, es suficiente larga.
    - Si fuera Prueba12345, informar que es correcta.
    - Si no, informar que es incorrecta.
- Si no, informar que es insegura y incorrecta.
"""

password = input("Ingresa la contraseña: ")

if (len(password) >= 8):
    print("Muy bien, contraseña suficientemente larga.")

    if (password == "Prueba12345"):
        print("Además, es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")

else:
    print("Tu contraseña es insegura.")
    print("Además, es incorrecta.")