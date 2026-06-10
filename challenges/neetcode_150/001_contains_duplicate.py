# ==================================================
# NeetCode 150 - Contains Duplicate
# Difficulty: Easy
# Topic: Arrays & Hashing
# ==================================================

class Solution:

    def hasDuplicate(self, nums):

        # Set para guardar números vistos
        seen = set()

        # Recorremos el array
        for num in nums:

            # Si ya existe, hay duplicado
            if num in seen:
                return True

            # Si no existe, lo agregamos
            seen.add(num)

        # No encontramos duplicados
        return False


# ==================================================
# Quick Notes
# ==================================================

# Objetivo:
# Detectar si un número aparece más de una vez.


# Fuerza Bruta:
#
# Comparar cada número con todos los demás.
#
# Time: O(n²)
# Space: O(1)


# Solución Óptima:
#
# Utilizar un Set.
#
# Los Sets NO permiten duplicados.
#
# Si el número ya está en el Set:
# -> return True
#
# Si no está:
# -> agregar al Set


# Ejemplo:
#
# [1, 2, 3, 2]
#
# seen = {}
#
# 1 -> agregar
# 2 -> agregar
# 3 -> agregar
# 2 -> ya existe
#
# return True


# Ejemplo:
#
# [1, 2, 3, 4]
#
# seen = {1,2,3,4}
#
# No hay repetidos
#
# return False


# Complejidad:
#
# Time: O(n)
# Space: O(n)


# Concepto Clave:
#
# Set = búsqueda O(1)
#
# En entrevistas:
# "¿Necesito saber rápidamente si ya vi algo?"
#
# Muchas veces la respuesta es:
# Set o Hash Map
