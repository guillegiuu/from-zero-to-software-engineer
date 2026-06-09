# ==================================================
# Challenge 07: Count Consonants
# ==================================================

# Objetivo:
# Contar cuántas consonantes contiene una cadena de texto.

# Conceptos:
# input(), for, if, strings, contador, operador in

# Análisis:
# El programa recorre cada carácter del texto.
# Si la letra no es una vocal (a, e, i, o, u),
# aumenta el contador en 1.
# Al finalizar, muestra la cantidad total
# de consonantes encontradas.

s = input().strip()

contador = 0

for c in s:
    if c not in "aeiou":
        contador += 1

print(contador)

# Output:
#
# Input:
# hello
#
# Output:
# 3
