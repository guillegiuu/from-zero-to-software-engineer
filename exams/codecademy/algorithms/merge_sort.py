# 🔀 Merge Sort (Codecademy Exam)
# Tema: Divide and Conquer
# Complejidad: O(n log n)

def merge_sort(unsorted):
    # Caso base: lista de 1 elemento
    if len(unsorted) <= 1:
        return unsorted

    # Dividir la lista en dos
    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    # Llamadas recursivas
    l_sorted = merge_sort(left)
    r_sorted = merge_sort(right)

    # Combinar resultados
    return merge(l_sorted, r_sorted)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


# 🧪 Test
print(merge_sort([2,4,3,5,1]))

# 💡 Explicación:
# Divide la lista en partes más chicas, las ordena recursivamente
# y luego las combina ordenadamente.
