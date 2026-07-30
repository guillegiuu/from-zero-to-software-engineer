# Chapter 13 — Files
# Ejemplo: recorrer un archivo línea por línea

# Abrimos el archivo en modo lectura
file = open("example.txt", "r")

# Recorremos cada línea del archivo
for line in file:
    # Mostramos cada línea
    print(line)

# Cerramos el archivo
file.close()
