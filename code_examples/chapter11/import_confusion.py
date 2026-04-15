# ⚠️ Error común: Import confusion

# ❌ Esto puede generar conflictos de nombres
from math import *

print(sqrt(16))  # Funciona, pero no es buena práctica

# ✔ Mejor forma
import math

print(math.sqrt(16))
