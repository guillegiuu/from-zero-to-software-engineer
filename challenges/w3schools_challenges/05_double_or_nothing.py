# ==================================================
# Challenge 05: Double or Nothing
# ==================================================

# Objetivo:
# Duplicar un número si es positivo.
# En caso contrario, mostrar 0.

# Conceptos:
# input(), if/else, operadores de comparación, print()

# Análisis:
# El programa verifica si el número es mayor que 0.
# Si lo es, imprime el doble de su valor.
# De lo contrario, imprime 0.

n = int(input())

if n > 0:
    print(n * 2)
else:
    print(0)

# Output:
#
# Input:
# 7
#
# Output:
# 14
