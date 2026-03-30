# 🔁 NESTED LOOPS (loops anidados)

# Ejemplo: combinaciones de dos listas
letters = ["A", "B", "C"]
numbers = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(letter, number)

# 🧠 Qué pasa:
# - el loop interno se ejecuta completo por cada iteración del externo
# - genera combinaciones:
# A 1, A 2, A 3
# B 1, B 2, B 3
# C 1, C 2, C 3
