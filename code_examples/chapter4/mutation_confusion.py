# Confusión con listas mutables

lista1 = [1, 2, 3]

# No crea una copia, apunta a la misma lista
lista2 = lista1

lista2.append(4)

print("lista1:", lista1)
print("lista2:", lista2)

# Ambas cambian → mismo objeto en memoria
