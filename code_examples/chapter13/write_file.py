# Chapter 13 — Files
# Ejemplo: escribir contenido en un archivo

# Abrimos el archivo en modo escritura ("w")
# OJO: si el archivo ya tenía contenido, se reemplaza
file = open("example.txt", "w")

# Escribimos texto dentro del archivo
file.write("Hola, este texto fue escrito desde Python.")

# Cerramos el archivo para guardar los cambios
file.close()
