# 🧩 LIST COMPREHENSIONS


# 🔹 Ejemplo 1: básico
numbers = [1, 2, 3, 4, 5]

squared = [n**2 for n in numbers]

print("Cuadrados:", squared)

# 🧠 Qué pasa:
# - recorre la lista
# - aplica una operación
# - guarda el resultado en una nueva lista


print("\n------------------\n")


# 🔹 Ejemplo 2: con condición
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]

print("Pares:", even_numbers)

# 🧠 Qué pasa:
# - filtra valores según condición
# - crea una nueva lista


print("\n------------------\n")


# 🔹 Ejemplo 3: versión equivalente con for
result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n)

print("Pares con for:", result)

# 🧠 Idea clave:
# - list comprehension = forma corta del for
