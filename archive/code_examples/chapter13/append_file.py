# Chapter 13 — Files
# Ejemplo: agregar contenido sin borrar lo anterior

# Abrimos el archivo en modo append ("a")
file = open("example.txt", "a")

# Agregamos contenido al final del archivo
file.write("\nNueva línea agregada con append.")

# Cerramos el archivo
file.close()
