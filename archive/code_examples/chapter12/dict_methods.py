# Métodos principales de diccionarios

usuario = {
    "nombre": "Guille",
    "edad": 25
}

# Acceso seguro
print(usuario.get("nombre"))
print(usuario.get("email"))  # None

# Obtener claves, valores e items
print(usuario.keys())
print(usuario.values())
print(usuario.items())
