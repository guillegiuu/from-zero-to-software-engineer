# 🔁 ITERACIÓN DE STRINGS

texto = "Python"

# Forma 1: recorrer por carácter
print("Recorrido por carácter:")
for char in texto:
    print(char)

# Forma 2: recorrer con índice
print("\nRecorrido por índice:")
for i in range(len(texto)):
    print(f"Índice {i}: {texto[i]}")

"""
Salida esperada:

Recorrido por carácter:
P
y
t
h
o
n

Recorrido por índice:
Índice 0: P
Índice 1: y
Índice 2: t
Índice 3: h
Índice 4: o
Índice 5: n
"""
