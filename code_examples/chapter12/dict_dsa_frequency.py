# Frequency map (conteo de elementos)

nums = [1, 1, 2, 3, 3, 3]

frecuencia = {}

for n in nums:
    if n in frecuencia:
        frecuencia[n] += 1
    else:
        frecuencia[n] = 1

print(frecuencia)
