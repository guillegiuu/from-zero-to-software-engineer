# 🧠 Challenge 02: Over Budget

📁 [Volver a Control Flow (Basic)](../README.md)  

💻 [Ver código](../solutions/challenge_02.py)  

📸 [Ver ejercicio](../images/control_flow_02.JPG)

---

## 📌 Problema
Dado un presupuesto y varios gastos, verificar si el total supera el límite y guardar el resultado en `over_budget`.

---

## 🔍 Lógica
1. Sumar todos los gastos → `total`  
2. Comparar `total` con `budget` usando `>`  
3. Guardar resultado booleano (`True` / `False`)

---

## 💡 Implementación

```python
total = food_bill + electricity_bill + internet_bill + rent

if total > budget:
    over_budget = True
else:
    over_budget = False
```

## 🐍 Versión Pythonic

```python
over_budget = total > budget
```

## ⏱ Complejidad
- Tiempo: O(1)
- Espacio: O(1)

## 🧠 Concepto clave
Comparación de valores con > para evaluar si un límite es superado.

## 🎯 Nota
Ejercicio básico de Control Flow para practicar acumulación de datos y lógica condicional.
