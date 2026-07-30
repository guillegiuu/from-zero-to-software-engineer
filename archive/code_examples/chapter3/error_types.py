# ERROR: tipos incompatibles

edad = "25"

resultado = edad + 5   # ❌ ERROR

print(resultado)

# ✔️ CORRECTO
edad = int("25")
resultado = edad + 5

print(resultado)
