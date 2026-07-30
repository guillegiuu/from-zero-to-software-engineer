# ⚠️ ERROR: OFF-BY-ONE (range)

# Queremos imprimir del 1 al 5

for i in range(1, 5):  # ❌ error
    print(i)

# 🧠 Problema:
# - range no incluye el último número
# - imprime: 1, 2, 3, 4

# ✅ Solución:
# range(1, 6)
