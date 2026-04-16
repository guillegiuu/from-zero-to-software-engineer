# 🧠 Challenge 04: Twice As Large

📁 [Volver a Control Flow (Basic)](../README.md)  

💻 [Ver código](../solutions/challenge_04.py)  

📸 [Ver ejercicio](../images/control_flow_04.JPG)

---

## 📌 Problema
Dado `num1` y `num2`, verificar si `num1` es mayor que el doble de `num2`.

---

## 🔍 Lógica
1. Multiplicar `num2` por `2`  
2. Comparar `num1` con ese resultado usando `>`  
3. Retornar `True` o `False`

---

## 💡 Implementación

```python
def twice_as_large(num1, num2):
    if num1 > (num2 * 2):
        return True
    else:
        return False
```

## 🐍 Versión Pythonic

```python
def twice_as_large(num1, num2):
    return num1 > (num2 * 2)
```

## ⏱ Complejidad
- Tiempo: O(1)
- Espacio: O(1)

## 🧠 Concepto clave
Comparación de valores con `>` y uso de multiplicación para construir una condición lógica.

## 🎯 Nota
Ejercicio básico para practicar funciones, comparaciones y evaluación de condiciones con expresiones aritméticas.

