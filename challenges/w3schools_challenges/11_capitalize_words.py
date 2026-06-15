# ==================================================
# CHALLENGE: Capitalize Each Word
# Objetivo: poner en mayúscula la primera letra
# de cada palabra de una oración.
# ==================================================

# Pedimos al usuario que escriba una oración.
# strip() elimina espacios sobrantes al inicio y al final.
sentence = input().strip()

# split() separa la oración en palabras.
# Ejemplo: "hello world" -> ["hello", "world"]
words = sentence.split()

# Creamos una lista vacía para guardar
# las palabras con la primera letra en mayúscula.
capitalized_words = []

# Recorremos cada palabra de la lista words.
for word in words:
    # capitalize() convierte la primera letra en mayúscula.
    # Luego guardamos esa palabra en la nueva lista.
    capitalized_words.append(word.capitalize())

# join() vuelve a unir las palabras en una sola oración.
# El " " indica que queremos separar cada palabra con un espacio.
result = " ".join(capitalized_words)

# Mostramos el resultado final.
print(result)
