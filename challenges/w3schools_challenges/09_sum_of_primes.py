# ==================================================
# Challenge 09: Sum of Primes
# ==================================================

# Objetivo:
# Calcular la suma de todos los números primos
# menores o iguales a un número dado.

# Conceptos:
# listas, while, for, range(), algoritmo Sieve of Eratosthenes

# Análisis:
# El programa utiliza la Criba de Eratóstenes
# para identificar números primos de manera eficiente.
# Primero marca todos los números como posibles primos.
# Luego descarta los múltiplos de cada primo encontrado.
# Finalmente suma todos los números que permanecen
# marcados como primos.

n = int(input())

is_prime = [True] * (n + 1)

is_prime[0] = False
is_prime[1] = False

p = 2

while p * p <= n:
    if is_prime[p]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
    p += 1

total = 0

for number in range(2, n + 1):
    if is_prime[number]:
        total += number

print(total)

# Output:
#
# Input:
# 10
#
# Output:
# 17
