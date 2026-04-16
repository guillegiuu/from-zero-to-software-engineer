🧠 Challenge 03: Large Power

🏠 [Volver a Control Flow (Basic)](../README.md)  

💻 [Ver código](../solutions/challenge_03.py)  

🖼️ [Ver ejercicio](../images/control_flow_03.JPG)

---

📌 Problema

Dado `base` y `exponent`, verificar si `base ** exponent` es mayor a 5000.

---

🔎 Lógica

1. Calcular `base ** exponent`
2. Comparar con 5000
3. Retornar `True` o `False`

---

💡 Implementación

```python
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
```

## 🐍 Versión Pythonic

```python
def large_power(base, exponent):
    return base ** exponent > 5000
```

## ⏱ Complejidad
- Tiempo: O(1)
- Espacio: O(1)

## 🧠 Concepto clave
- Operador de potencia: `**`
- Uso de funciones (`def` + `return`)

## 🎯 Nota
Ejercicio básico para introducir funciones y encapsular lógica reutilizable.
