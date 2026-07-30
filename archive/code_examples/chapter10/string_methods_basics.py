# 🧰 MÉTODOS BÁSICOS DE STRINGS

texto = "Hola mundo desde Python"

# split()
palabras = texto.split()
print("Split:", palabras)

# join()
unido = " - ".join(palabras)
print("Join:", unido)

# strip()
texto_con_espacios = "   Python   "
print("Strip:", texto_con_espacios.strip())

"""
Salida esperada:

Split: ['Hola', 'mundo', 'desde', 'Python']
Join: Hola - mundo - desde - Python
Strip: Python
"""
