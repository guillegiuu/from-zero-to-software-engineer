# ==========================================
# Challenge 12: Two Sum
# ==========================================
#
# Objetivo:
# Encontrar dos números en una lista que
# sumen el valor objetivo (target) y
# mostrar sus índices.
#
# Conceptos:
# arrays, bucles for, índices,
# comparación de elementos, fuerza bruta
#
# Análisis:
# El programa recorre todas las parejas
# posibles de números usando dos bucles.
#
# El primer bucle selecciona un número.
# El segundo bucle compara ese número con
# todos los siguientes elementos de la lista.
#
# Si la suma de ambos números es igual al
# target, se imprimen los índices y el
# programa termina.
#
# Complejidad:
# Tiempo: O(n²)
# Memoria: O(1)
# ==========================================

# Leemos la primera línea de entrada
first_line = input().split()

# Convertimos N (cantidad de números)
# y T (valor objetivo) a enteros
n, t = int(first_line[0]), int(first_line[1])

# Leemos los N números y los guardamos
# dentro de una lista
numbers = [int(input()) for _ in range(n)]

# Recorremos cada posición de la lista
for i in range(n):

    # Comparamos con los elementos
    # que están después de i
    for j in range(i + 1, n):

        # Verificamos si la suma es igual
        # al valor objetivo
        if numbers[i] + numbers[j] == t:

            # Mostramos los índices
            print(i, j)

            # Terminamos el programa
            exit()
