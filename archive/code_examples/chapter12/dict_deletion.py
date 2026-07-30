# Eliminación en diccionarios

usuario = {
    "nombre": "Guille",
    "edad": 25
}

# Usando del (no devuelve nada)
del usuario["edad"]

# Usando pop (devuelve el valor)
nombre = usuario.pop("nombre")

print(nombre)
print(usuario)
