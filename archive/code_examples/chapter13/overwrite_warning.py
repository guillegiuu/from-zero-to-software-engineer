# Chapter 13 — Files
# Error común: usar "w" y borrar contenido anterior

# Abrimos el archivo en modo escritura
# Esto reemplaza todo el contenido anterior del archivo
with open("example.txt", "w") as file:
    # Escribimos nuevo contenido
    file.write("Este texto reemplaza todo lo anterior.")

print("Archivo sobrescrito correctamente.")
