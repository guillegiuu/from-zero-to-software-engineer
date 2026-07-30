# missing_return.py
# Error común: pensar que una función devuelve algo cuando solo lo imprime

def sumar(a, b):
    print(a + b)  # Solo muestra el resultado, no lo devuelve

resultado = sumar(2, 3)

print("Valor guardado en resultado:", resultado)
