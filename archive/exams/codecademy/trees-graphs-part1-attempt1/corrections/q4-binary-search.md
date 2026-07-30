# 🔍 Q4 — Binary Search (Recursivo)

## 📌 Tema
Binary Search recursivo

---

## ❌ Error
Condición base incorrecta

---

## ✅ Corrección

Caso base correcto:

// left_pointer > right_pointer → return None

---

## 🧠 Clave

- Si el rango es inválido → no existe el elemento  
- Comparar con `mid` y ajustar límites:

// mid_val > target → buscar izquierda  
// mid_val < target → buscar derecha  

---

## ⚠️ Trampa

Confundir la condición:

❌ left <= right  
✔️ left > right (corte de la recursión)

---

## 🎯 Regla

- Siempre definir bien el caso base  
- Binary Search termina cuando el rango se rompe
