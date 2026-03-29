# Métodos de listas en Python

numeros = [3, 1, 4, 1, 5]

print("Lista original:", numeros)

# append() → agregar al final
numeros.append(9)
print("Después de append:", numeros)

# insert() → agregar en posición específica
numeros.insert(1, 10)
print("Después de insert:", numeros)

# count() → contar ocurrencias
cantidad = numeros.count(1)
print("Cantidad de 1:", cantidad)

# sort() → ordenar
numeros.sort()
print("Lista ordenada:", numeros)

# reverse() → invertir
numeros.reverse()
print("Lista invertida:", numeros)
