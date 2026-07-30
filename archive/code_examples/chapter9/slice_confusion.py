# ⚠️ ERROR COMÚN: Confusión con slicing

texto = "Python"

# Ejemplo 1
print(texto[0:2])  # Py

# Ejemplo 2
print(texto[2:5])  # tho

# Ejemplo 3 (sin inicio)
print(texto[:3])   # Pyt

# Ejemplo 4 (sin fin)
print(texto[3:])   # hon

# 🔥 Regla de oro:
# start incluye, end NO incluye

"""
Salida esperada:

Py
tho
Pyt
hon
"""
