# Ordenar listas en Python

numeros = [5, 2, 9, 1, 3]

print("Lista original:", numeros)

# Orden ascendente
numeros.sort()
print("Orden ascendente:", numeros)

# Orden descendente
numeros.sort(reverse=True)
print("Orden descendente:", numeros)

# sorted() → no modifica la original
nueva_lista = sorted(numeros)
print("Nueva lista ordenada:", nueva_lista)
print("Lista original después de sorted():", numeros)
