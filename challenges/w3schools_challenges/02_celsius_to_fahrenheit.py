# ==================================================
# Challenge 02: Celsius to Fahrenheit
# ==================================================

# Objetivo:
# Convertir una temperatura de Celsius a Fahrenheit
# utilizando la fórmula de conversión.

# Conceptos:
# input(), variables, operadores aritméticos, print()

# Análisis:
# El programa recibe una temperatura en Celsius,
# aplica la fórmula de conversión y muestra
# el resultado en pantalla.

celsius = int(input())

fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

# Output:
#
# Input:
# 25
#
# Output:
# 25 Celsius = 77.0 Fahrenheit
