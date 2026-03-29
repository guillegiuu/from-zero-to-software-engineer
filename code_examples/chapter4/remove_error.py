# Error: intentar eliminar un valor que no existe

numeros = [1, 2, 3]

print("Lista:", numeros)

# Esto genera error
print("Intentando eliminar 5:")
numeros.remove(5)  # ValueError
