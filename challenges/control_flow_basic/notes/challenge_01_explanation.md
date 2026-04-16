# 🧠 Challenge 01: Not Sum To Ten

## 📌 Problema
Dado `num1` y `num2`, verificar si su suma **NO es igual a 10** y guardar el resultado en `not_ten`.

---

## 🔍 Lógica
1. Calcular: `num1 + num2`  
2. Comparar con 10 usando `!=`  
3. Guardar el resultado (True / False)

---

## 💡 Implementación

```python
if (num1 + num2) != 10:
    not_ten = True
else:
    not_ten = False
```

## 🐍 Versión Pythonic
```python
not_ten = (num1 + num2) != 10
```

## ⏱ Complejidad
- Tiempo: O(1)
- Espacio: O(1)

## 🧠 Concepto clave
Operador de desigualdad: !=

## 🎯 Nota
Ejercicio básico de Control Flow para practicar condiciones y lógica booleana.
