# Chapter 13 — Files
# Ejemplo: leer un archivo CSV

# Importamos el módulo csv
import csv

# Abrimos el archivo CSV
with open("students.csv", "r") as file:
    # Creamos un lector CSV
    reader = csv.reader(file)

    # Recorremos cada fila del archivo
    for row in reader:
        # Mostramos la fila completa
        print(row)
