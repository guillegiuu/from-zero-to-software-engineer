# ⛔ BREAK y ⏭️ CONTINUE


# 🔹 Ejemplo 1: break
print("Ejemplo con break:")

for i in range(10):
    if i == 5:
        break  # corta el loop completamente
    print(i)

# 🧠 Resultado:
# 0, 1, 2, 3, 4


print("\n------------------\n")


# 🔹 Ejemplo 2: continue
print("Ejemplo con continue:")

for i in range(10):
    if i == 5:
        continue  # salta esta iteración
    print(i)

# 🧠 Resultado:
# 0, 1, 2, 3, 4, 6, 7, 8, 9
