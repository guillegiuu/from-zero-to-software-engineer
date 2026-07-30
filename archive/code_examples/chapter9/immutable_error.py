# ❌ ERROR COMÚN: Strings son inmutables

texto = "Hola"

# Esto rompe:
# texto[0] = "H"

# Forma correcta:
nuevo_texto = "H" + texto[1:]

print("Original:", texto)
print("Nuevo:", nuevo_texto)

"""
Salida esperada:

Original: Hola
Nuevo: Hola
"""

# 🔥 Regla clave:
# No se modifica el string original, se crea uno nuevo
