# Archivo: dotdot_confusion.py

# --------------------------------------------------
# ¿Qué muestra este archivo?
# --------------------------------------------------
# Error común: confusión con "cd .."
# Mucha gente no entiende bien cómo subir en el filesystem.

# --------------------------------------------------
# ESTRUCTURA (ASCII)
# --------------------------------------------------

# /
# └── home
#     └── guille
#         └── proyectos
#             └── app.py

# --------------------------------------------------
# SITUACIÓN INICIAL
# --------------------------------------------------

# Estás en:
# /home/guille/proyectos

# --------------------------------------------------
# USO DE cd ..
# --------------------------------------------------

# Comando:
# cd ..

# Resultado:
# /home/guille

# 👉 Subiste UN nivel

# --------------------------------------------------
# ERROR COMÚN
# --------------------------------------------------

# Pensar que "cd .." vuelve al inicio ❌
# Pensar que baja de carpeta ❌

# --------------------------------------------------
# EJEMPLOS CLAROS
# --------------------------------------------------

# Estás en:
# /home/guille/proyectos

# cd .. → /home/guille
# cd .. → /home
# cd .. → /

# --------------------------------------------------
# VISUAL (ASCII paso a paso)
# --------------------------------------------------

# /home/guille/proyectos
#           ↑ cd ..

# /home/guille
#        ↑ cd ..

# /home
#    ↑ cd ..

# /

# --------------------------------------------------
# IDEA CLAVE
# --------------------------------------------------
# "cd .." SIEMPRE significa:
# → subir un nivel en la estructura

# --------------------------------------------------
# TIP PRO
# --------------------------------------------------
# Para subir varios niveles rápido:
# cd ../../

# Ejemplo:
# /home/guille/proyectos
# cd ../../ → /home
