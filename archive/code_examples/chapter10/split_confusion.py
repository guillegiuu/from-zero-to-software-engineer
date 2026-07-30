# ⚠️ ERROR COMÚN: split()

texto = "Hola mundo Python"

# Caso normal
print(texto.split())  # separa por espacios

# Confusión común
texto2 = "Hola,mundo,Python"
print(texto2.split(","))  # separa por coma

"""
Salida esperada:

['Hola', 'mundo', 'Python']
['Hola', 'mundo', 'Python']
"""

# 🔥 Regla:
# split() separa por el separador que le indiques (default = espacio)
