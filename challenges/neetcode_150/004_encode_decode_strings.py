# ==================================================
# Challenge: Encode and Decode Strings
# Difficulty: Medium (NeetCode)
# Pattern: String Design
# ==================================================

class Solution:

    def encode(self, strs):
        # String donde construiremos el resultado final
        encoded_string = ""

        # Recorremos cada string de la lista
        for string in strs:

            # Obtenemos la longitud del string actual
            length = len(string)

            # Formato: longitud#string
            encoded_string += f"{length}#{string}"

        # Devolvemos el string codificado
        return encoded_string


    def decode(self, s):
        # Lista donde guardaremos los strings recuperados
        decoded_strings = []

        # Puntero que recorre el string codificado
        position = 0

        # Mientras no lleguemos al final
        while position < len(s):

            # Encontramos el próximo #
            hash_index = s.find("#", position)

            # Extraemos la longitud y la convertimos a entero
            length = int(s[position:hash_index])

            # El string comienza después del #
            start = hash_index + 1

            # Leemos exactamente "length" caracteres
            decoded_string = s[start:start + length]

            # Guardamos el string recuperado
            decoded_strings.append(decoded_string)

            # Saltamos al siguiente bloque
            position = start + length

        # Devolvemos la lista original
        return decoded_strings


# ==================================================
# Quick Notes
# ==================================================

# ENCODE
# Lista -> String
#
# "cat"   -> "3#cat"
# "hello" -> "5#hello"
# "a"     -> "1#a"
#
# Resultado:
# "3#cat5#hello1#a"


# DECODE
#
# 1. Buscar #
# 2. Obtener la longitud
# 3. Leer esa cantidad de caracteres
# 4. Guardar el string
# 5. Avanzar position
# 6. Repetir


# Ejemplo:
#
# "3#cat5#hello1#a"
#
# ↓
#
# ["cat", "hello", "a"]


# Complejidad
#
# Time:  O(n)
# Space: O(n)
#
# n = cantidad total de caracteres


# Idea clave:
#
# No confiamos en separadores.
# Confiamos en la longitud del string.
#
# Esto evita problemas cuando aparecen:
# "#", números o cualquier otro carácter
# dentro del texto original.
