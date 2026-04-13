# Archivo: basic_navigation.py

# --------------------------------------------------
# ¿Qué hace este archivo?
# --------------------------------------------------
# Este archivo muestra comandos de terminal usando comentarios,
# junto con ejemplos visuales en ASCII para entender mejor.

# --------------------------------------------------
# ESTRUCTURA DEL FILESYSTEM (ASCII)
# --------------------------------------------------

# /
# ├── home
# │   └── guille
# │       ├── proyectos
# │       │   └── app.py
# │       └── notas.txt
# └── etc

# --------------------------------------------------
# 1) pwd
# --------------------------------------------------
# Muestra en qué carpeta estás actualmente

# Ejemplo:
# Estás en:
# /home/guille

# Comando:
# pwd

# Output esperado:
# /home/guille

# --------------------------------------------------
# 2) ls
# --------------------------------------------------
# Lista archivos y carpetas del directorio actual

# Estás en /home/guille

# Comando:
# ls

# Output:
# proyectos  notas.txt

# --------------------------------------------------
# 3) cd (navegación)
# --------------------------------------------------

# Estás en:
# /home/guille

# cd proyectos  → bajás

# Resultado:
# /home/guille/proyectos

# cd .. → subís

# Resultado:
# /home/guille

# cd / → raíz

# Resultado:
# /

# cd ~ → home

# Resultado:
# /home/guille
