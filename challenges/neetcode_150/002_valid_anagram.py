# ==================================================
# NeetCode 150 - Valid Anagram
# Difficulty: Easy
# Topic: Hash Table / String
# ==================================================

class Solution:

    def isAnagram(self, s, t):

        # Si tienen distinta longitud, no puede ser anagrama
        if len(s) != len(t):
            return False

        # Contador de letras de s
        countS = {}

        # Contador de letras de t
        countT = {}

        # Contamos letras de s
        for char in s:
            countS[char] = 1 + countS.get(char, 0)

        # Contamos letras de t
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Comparamos ambos diccionarios
        return countS == countT


# ==================================================
# Quick Notes
# ==================================================

# Objetivo:
# Verificar si dos strings contienen
# exactamente las mismas letras.


# Anagrama:
#
# "racecar"
# "carrace"
#
# Mismas letras
# Distinto orden
#
# Resultado: True


# Fuerza Bruta:
#
# Ordenar ambos strings
#
# sorted(s)
# sorted(t)
#
# Comparar resultados
#
# Time: O(n log n)


# Solución Óptima:
#
# Contar cuántas veces aparece
# cada letra en ambos strings.
#
# Si los conteos coinciden:
# -> True
#
# Si no coinciden:
# -> False


# Ejemplo:
#
# s = "jar"
# t = "jam"
#
# countS:
# {
#   "j":1,
#   "a":1,
#   "r":1
# }
#
# countT:
# {
#   "j":1,
#   "a":1,
#   "m":1
# }
#
# Son distintos
#
# return False


# Complejidad:
#
# Time: O(n)
# Space: O(n)


# Concepto Clave:
#
# Hash Map / Dictionary
#
# Clave  -> letra
# Valor  -> cantidad de apariciones
#
# Ejemplo:
#
# "banana"
#
# {
#   "b":1,
#   "a":3,
#   "n":2
# }
