# ==================================================
# Challenge 04: Make a Username
# ==================================================

# Objetivo:
# Crear un nombre de usuario uniendo nombre y apellido
# en minúsculas, además de mostrar sus iniciales.

# Conceptos:
# input(), strings, .lower(), .upper(), índices [0], print()

# Análisis:
# El programa recibe un nombre y un apellido.
# Luego genera un username en minúsculas sin espacios
# y obtiene las iniciales tomando la primera letra
# de cada palabra en mayúsculas.

first_name = input().strip()
last_name = input().strip()

username = first_name.lower() + last_name.lower()

initials = first_name[0].upper() + last_name[0].upper()

print("Username:", username)
print("Initials:", initials)

# Output:
#
# Input:
# Kai
# Tove
#
# Output:
# Username: kaitove
# Initials: KT
