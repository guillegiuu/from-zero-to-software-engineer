# ==================================================
# CHALLENGE: Valid Palindrome
# Objetivo: verificar si un string es palíndromo.
# Ignoramos espacios, símbolos y mayúsculas/minúsculas.
# ==================================================


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Puntero izquierdo: arranca al inicio del string.
        left = 0

        # Puntero derecho: arranca al final del string.
        right = len(s) - 1

        # Mientras los punteros no se crucen, seguimos comparando.
        while left < right:

            # Si el carácter de la izquierda NO es letra ni número,
            # lo ignoramos y avanzamos.
            while left < right and not s[left].isalnum():
                left += 1

            # Si el carácter de la derecha NO es letra ni número,
            # lo ignoramos y retrocedemos.
            while left < right and not s[right].isalnum():
                right -= 1

            # Comparamos ambos caracteres en minúscula.
            # Si son distintos, no es palíndromo.
            if s[left].lower() != s[right].lower():
                return False

            # Si coinciden, movemos ambos punteros hacia el centro.
            left += 1
            right -= 1

        # Si nunca encontramos diferencias, es palíndromo.
        return True


# =========================
# TESTS
# =========================

solution = Solution()

print(solution.isPalindrome("Was it a car or a cat I saw?"))
# True

print(solution.isPalindrome("tab a cat"))
# False

print(solution.isPalindrome("A man, a plan, a canal: Panama"))
# True


# ==================================================
# ANÁLISIS ULTRA MACHETE
# ==================================================

# 1) Usamos dos punteros:
#    left empieza al inicio.
#    right empieza al final.

# 2) Ignoramos todo lo que NO sea letra o número:
#    espacios, signos, comas, puntos, etc.
#    Para eso usamos isalnum().

# 3) Convertimos a minúscula con lower()
#    para que "A" y "a" cuenten como iguales.

# 4) Si dos caracteres no coinciden:
#    return False

# 5) Si los punteros llegan al centro sin fallar:
#    return True

# Complejidad:
# Tiempo: O(n)
# Memoria: O(1)

# Regla mental:
# Comparar extremos + avanzar al centro = Two Pointers.
