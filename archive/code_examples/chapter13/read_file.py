# Chapter 13 — Files
# Ejemplo: leer un archivo completo

# Abrimos el archivo en modo lectura ("r")
file = open("example.txt", "r")

# Leemos todo el contenido del archivo
content = file.read()

# Mostramos el contenido en pantalla
print(content)

# Cerramos el archivo manualmente
file.close()
