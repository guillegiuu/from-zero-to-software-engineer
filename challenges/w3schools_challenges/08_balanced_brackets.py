# ==================================================
# Challenge 08: Balanced Brackets
# ==================================================

# Objetivo:
# Verificar si una secuencia de paréntesis y corchetes
# está correctamente balanceada.

# Conceptos:
# strings, listas, for, if/else, append(), pop()

# Análisis:
# El programa utiliza una lista como pila (stack).
# Cada bracket de apertura se guarda en la pila.
# Cuando aparece un bracket de cierre, se verifica
# si coincide con el último bracket abierto.
# Si todos coinciden y no quedan aperturas pendientes,
# la secuencia está balanceada.

s = input().strip()

stack = []
balanced = True

for char in s:

    if char == "(" or char == "[":
        stack.append(char)

    elif char == ")" or char == "]":

        if not stack:
            balanced = False
            break

        last = stack.pop()

        if char == ")" and last != "(":
            balanced = False
            break

        if char == "]" and last != "[":
            balanced = False
            break

if stack:
    balanced = False

if balanced:
    print("Yes")
else:
    print("No")

# Output:
#
# Input:
# ([])
#
# Output:
# Yes
