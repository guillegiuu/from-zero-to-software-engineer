# Chapter 13 — Files
# Ejemplo: leer una sola línea

# Abrimos el archivo en modo lectura
file = open("example.txt", "r")

# Leemos solo la primera línea del archivo
first_line = file.readline()

# Mostramos esa línea
print(first_line)

# Cerramos el archivo
file.close()
