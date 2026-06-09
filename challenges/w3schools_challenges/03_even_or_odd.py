# ==================================================
# Challenge 03: Even or Odd
# ==================================================

# Objetivo:
# Determinar si un número es par o impar.

# Conceptos:
# input(), if/else, operador %, print()

# Análisis:
# Un número es par cuando el resto de dividirlo por 2
# es igual a 0. En caso contrario, es impar.

n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
#
# Input:
# 7
#
# Output:
# Odd
