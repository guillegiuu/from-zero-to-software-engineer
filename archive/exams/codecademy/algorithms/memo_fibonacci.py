# 🔢 Fibonacci con Memoization (Codecademy Exam)
# Tema: Dynamic Programming
# Complejidad: O(n)

memo = {}

def memo_fibonacci(number):
    ans = None

    # Si ya está calculado
    if number in memo:
        ans = memo[number]

    # Casos base
    elif number == 0 or number == 1:
        ans = number

    # Recursión + memo
    else:
        ans = memo_fibonacci(number - 1) + memo_fibonacci(number - 2)
        memo[number] = ans

    return ans


# 🧪 Test
print(memo_fibonacci(20))
print(memo_fibonacci(100))

# 💡 Explicación:
# Guarda resultados en un diccionario para evitar cálculos repetidos.
