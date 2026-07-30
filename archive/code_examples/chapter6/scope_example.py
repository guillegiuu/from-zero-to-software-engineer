# scope_example.py
# Ejemplo de variables locales y globales (scope)

x = 10  # Variable global

def mostrar_valor():
    x = 5  # Variable local
    print("Dentro de la función:", x)

mostrar_valor()

print("Fuera de la función:", x)
