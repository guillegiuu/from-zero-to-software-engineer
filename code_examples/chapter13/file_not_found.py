# Chapter 13 — Files
# Error común: intentar abrir un archivo que no existe

try:
    # Intentamos abrir un archivo inexistente
    file = open("missing_file.txt", "r")

    # Intentamos leer su contenido
    content = file.read()

    # Mostramos el contenido
    print(content)

    # Cerramos el archivo
    file.close()

except FileNotFoundError:
    # Este bloque se ejecuta si el archivo no existe
    print("Error: el archivo no existe.")
