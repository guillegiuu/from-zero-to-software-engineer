# ⚡ Quick Sort (Codecademy Exam)
# Tema: Divide and Conquer
# Complejidad: O(n log n) promedio

from random import randrange

def quicksort(lst, start, end):
    if start >= end:
        return

    # Elegir pivote aleatorio
    pivot_ptr = randrange(start, end + 1)
    pivot_element = lst[pivot_ptr]

    # Mover pivote al final
    lst[end], lst[pivot_ptr] = lst[pivot_ptr], lst[end]

    less_than_ptr = start

    # Reordenar elementos
    for i in range(start, end):
        if lst[i] < pivot_element:
            lst[i], lst[less_than_ptr] = lst[less_than_ptr], lst[i]
            less_than_ptr += 1

    # Colocar pivote en posición final
    lst[end], lst[less_than_ptr] = lst[less_than_ptr], lst[end]

    # Recursión izquierda y derecha
    quicksort(lst, start, less_than_ptr - 1)
    quicksort(lst, less_than_ptr + 1, end)


# 🧪 Test
l = [4,8,2,5,1,9,0,7,3,6]
quicksort(l, 0, len(l)-1)
print(l)

# 💡 Explicación:
# Usa un pivote para dividir la lista en menores y mayores
# y aplica recursión sobre cada parte.
