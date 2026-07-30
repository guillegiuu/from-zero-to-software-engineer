# 🔍 BÚSQUEDA Y REEMPLAZO

texto = "Hola mundo"

# find()
print("Índice de 'm':", texto.find("m"))
print("Índice de 'z':", texto.find("z"))  # no existe

# replace()
nuevo_texto = texto.replace("mundo", "Python")
print("Replace:", nuevo_texto)

"""
Salida esperada:

Índice de 'm': 5
Índice de 'z': -1
Replace: Hola Python
"""
