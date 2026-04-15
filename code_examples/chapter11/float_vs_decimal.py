# ⚠️ Error común: Float vs Decimal

from decimal import Decimal

# ❌ Problema con float
resultado_float = 0.1 + 0.2
print("Resultado float:", resultado_float)

# ✔ Solución con Decimal
resultado_decimal = Decimal("0.1") + Decimal("0.2")
print("Resultado decimal:", resultado_decimal)
