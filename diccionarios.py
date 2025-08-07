#Primera forma de crear un diccionário (key: value)
diccionario = {
    "Nombre": "Sara",
    "Edad": 28,
    "Documento": 456234
}

print(diccionario)

#Segunda forma de crear un diccionário
diccionario_seg = dict(Nombre="Paola",
                       Edad=37,
                       Documento=2394534)

print(diccionario_seg)

#Tercera forma de crear un diccionário
diccionario_ter = dict([
    ("Nombre", "Jose"),
    ("Edad", 24),
    ("Documento", 232345)
])

print(diccionario_ter)

print("")

#Métodos
inventario = {"Manzanas": 235, "Peras": 400, "Naranjas": 250, "Sandias": 500}

print(inventario.keys())
print(inventario.values())
print(inventario.items())