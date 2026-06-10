# ==================================================
# NeetCode 150 - Two Sum
# Difficulty: Easy
# Topic: Arrays & Hashing
# ==================================================

class Solution:

    def twoSum(self, nums, target):

        # Número -> índice
        seen = {}

        # Recorremos array
        for index, num in enumerate(nums):

            # Número que necesitamos encontrar
            complement = target - num

            # Si ya lo vimos, encontramos la respuesta
            if complement in seen:
                return [seen[complement], index]

            # Guardamos número actual e índice
            seen[num] = index


# ==================================================
# Quick Notes
# ==================================================

# Objetivo:
#
# Encontrar dos números cuya suma
# sea igual al target.
#
# Devolver sus índices.


# Ejemplo:
#
# nums = [3,4,5,6]
# target = 7
#
# 3 + 4 = 7
#
# return [0,1]


# Fuerza Bruta:
#
# Comparar cada número con todos
# los demás números.
#
# Time: O(n²)
# Space: O(1)


# Solución Óptima:
#
# Utilizar Hash Map.
#
# Clave  -> número
# Valor  -> índice


# Idea Principal:
#
# target = num + complement
#
# complement = target - num
#
# Si ya vimos complement:
# -> respuesta encontrada


# Ejemplo:
#
# nums = [3,4,5,6]
# target = 7
#
# index=0
# num=3
#
# complement=4
#
# seen={}
#
# guardar:
# {3:0}
#
#
# index=1
# num=4
#
# complement=3
#
# 3 ya existe
#
# return [0,1]


# Complejidad:
#
# Time: O(n)
# Space: O(n)


# Concepto Clave:
#
# Hash Map = búsqueda O(1)
#
# Guardamos:
#
# número -> índice
#
# para encontrar rápidamente
# el complemento.


# Fórmula importante:
#
# complement = target - num
