# arguments_types.py
# Tipos de argumentos en funciones

# Función con dos parámetros
def presentar(nombre, edad):
    print("Nombre:", nombre)
    print("Edad:", edad)

# 1. Argumentos posicionales (según el orden)
presentar("Guille", 25)

print("-----")

# 2. Argumentos nombrados (keyword)
presentar(edad=25, nombre="Guille")

print("-----")

# 3. Valores por defecto
def saludar(nombre="Invitado"):
    print("Hola,", nombre)

saludar()          # Usa valor por defecto
saludar("Guille")  # Sobrescribe el valor
