# Chapter 13 — Files
# Ejemplo: usar with open()

# with open() abre el archivo y lo cierra automáticamente
with open("example.txt", "r") as file:
    # Leemos el contenido del archivo
    content = file.read()

    # Mostramos el contenido
    print(content)

# No hace falta usar file.close()
