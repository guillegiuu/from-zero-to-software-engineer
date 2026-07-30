# 💰 Decimal Precision

from decimal import Decimal

# Suma con float (puede fallar)
print("Float:", 0.1 + 0.2)

# Suma con Decimal (exacta)
print("Decimal:", Decimal("0.1") + Decimal("0.2"))
