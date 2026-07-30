# Error al usar clave mutable

mi_dict = {}

# Esto rompe porque la lista es mutable
mi_dict[[1, 2, 3]] = "valor"
