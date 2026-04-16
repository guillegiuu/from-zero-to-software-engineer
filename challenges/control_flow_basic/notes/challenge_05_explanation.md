# 🧠 Challenge 05: Divisible By Ten

📁 [Volver a Control Flow (Basic)](../README.md)  

💻 [Ver código](../solutions/challenge_05.py) 

📸 [Ver ejercicio](../images/control_flow_05.JPG)

---

## 📌 Problema
Dado `num`, verificar si es divisible por `10`.

---

## 🔍 Lógica
1. Calcular `num % 10`  
2. Verificar si el resto es `0`  
3. Retornar `True` o `False`

---

## 💡 Implementación

```python
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
```

## 🐍 Versión Pythonic

```python
def divisible_by_ten(num):
    return num % 10 == 0
```

## ⏱ Complejidad
- Tiempo: O(1)
- Espacio: O(1)

## 🧠 Concepto clave
Uso del operador módulo `%` para verificar divisibilidad.

## 🎯 Nota
Ejercicio básico para practicar funciones, condición `if/else` y aritmética modular.

