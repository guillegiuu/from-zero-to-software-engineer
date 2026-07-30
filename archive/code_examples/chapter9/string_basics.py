# 🔤 STRING BASICS

# Creación de strings
texto = "Hola"
print("String:", texto)

# Indexing (acceder a posiciones)
print("Primer letra:", texto[0])
print("Última letra:", texto[-1])

# Slicing (cortes)
print("Primeras 2 letras:", texto[0:2])

# Regla importante:
# start incluye, end NO incluye

# Longitud
print("Longitud:", len(texto))

# Operaciones básicas
print("Concatenar:", "Hola" + " Mundo")
print("Repetir:", "Ha" * 3)

"""
Salida esperada:

String: Hola
Primer letra: H
Última letra: a
Primeras 2 letras: Ho
Longitud: 4
Concatenar: Hola Mundo
Repetir: HaHaHa
"""
