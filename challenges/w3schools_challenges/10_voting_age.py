# ==================================================
# Challenge 10: Voting Age
# ==================================================

# Objetivo:
# Determinar si una persona tiene edad suficiente
# para votar según la edad ingresada.

# Conceptos:
# input(), if/else, operadores de comparación, f-strings

# Análisis:
# El programa recibe un nombre y una edad.
# Si la edad es 18 o mayor, indica que puede votar.
# En caso contrario, informa que no puede votar.

name = input().strip()
age = int(input())

if age >= 18:
    print(f"{name} can vote")
else:
    print(f"{name} cannot vote")

# Output:
#
# Input:
# Robin
# 16
#
# Output:
# Robin cannot vote
