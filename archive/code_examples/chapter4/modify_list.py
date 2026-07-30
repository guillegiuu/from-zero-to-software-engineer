# Modificar listas en Python

numeros = [1, 2, 3]

print("Lista original:", numeros)

# Modificar un valor por índice
numeros[0] = 10
print("Después de modificar índice 0:", numeros)

# Agregar elemento al final
numeros.append(4)
print("Después de append:", numeros)

# Eliminar por valor
numeros.remove(2)
print("Después de remove:", numeros)

# Eliminar por índice
numeros.pop(1)
print("Después de pop:", numeros)
