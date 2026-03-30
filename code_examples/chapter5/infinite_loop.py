# ⚠️ ERROR: LOOP INFINITO

x = 0

while x < 5:
    print("x:", x)
    # ❌ falta actualizar x → loop infinito

# 🧠 Problema:
# - la condición siempre es True
# - nunca cambia x

# ✅ Solución:
# agregar:
# x += 1
