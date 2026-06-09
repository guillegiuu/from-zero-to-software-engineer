# ==================================================
# Challenge 06: Reverse String
# ==================================================

# Objetivo:
# Invertir una cadena de texto sin utilizar
# funciones o métodos de reversa incorporados.

# Conceptos:
# input(), for, range(), len(), índices, print()

# Análisis:
# El programa recorre el texto desde el último
# carácter hasta el primero e imprime cada letra
# en orden inverso para construir la cadena invertida.

s = input().strip()

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")

# Output:
#
# Input:
# hello
#
# Output:
# olleh
