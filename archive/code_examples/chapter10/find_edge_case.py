# ⚠️ ERROR COMÚN: find()

texto = "Python"

# Caso donde existe
indice = texto.find("t")
print("Índice de 't':", indice)

# Caso donde NO existe
indice = texto.find("z")

if indice == -1:
    print("No encontrado")
else:
    print("Encontrado en:", indice)

"""
Salida esperada:

Índice de 't': 2
No encontrado
"""

# 🔥 Regla:
# find() devuelve -1 si no encuentra el valor
