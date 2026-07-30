# Chapter 13 — Files
# Ejemplo: leer un archivo JSON

# Importamos el módulo json
import json

# Abrimos el archivo JSON
with open("data.json", "r") as file:
    # Convertimos el JSON en datos de Python
    data = json.load(file)

# Mostramos los datos
print(data)
