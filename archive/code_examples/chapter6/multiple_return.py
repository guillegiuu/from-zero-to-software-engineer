# multiple_return.py
# Ejemplo de función con múltiples valores de retorno

def operaciones(a, b):
    suma = a + b
    multiplicacion = a * b
    return suma, multiplicacion

# Guardamos ambos resultados
suma, multi = operaciones(2, 3)

print("Suma:", suma)
print("Multiplicación:", multi)
