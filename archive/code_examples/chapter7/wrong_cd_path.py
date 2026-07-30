# Archivo: wrong_cd_path.py

# --------------------------------------------------
# ¿Qué muestra este archivo?
# --------------------------------------------------
# Error común: intentar entrar a una carpeta que NO existe.

# --------------------------------------------------
# ESTRUCTURA (ASCII)
# --------------------------------------------------

# /home/guille
# ├── proyectos
# └── notas.txt

# --------------------------------------------------
# ERROR
# --------------------------------------------------

# Estás en:
# /home/guille

# Intentás:
# cd proyecto

# ❌ ERROR (porque la carpeta real es "proyectos")

# Output típico:
# cd: no such file or directory: proyecto

# --------------------------------------------------
# SOLUCIÓN
# --------------------------------------------------

# Primero verificás qué hay:
# ls

# Output:
# proyectos  notas.txt

# Ahora sí:
# cd proyectos

# Resultado:
# /home/guille/proyectos

# --------------------------------------------------
# IDEA CLAVE
# --------------------------------------------------
# Siempre antes de usar cd:
# 1. Usar ls para ver nombres correctos
# 2. Respetar mayúsculas/minúsculas
# 3. Evitar escribir "a ojo"

# --------------------------------------------------
# REGLA PRO
# --------------------------------------------------
# Si dudás:
# → usá TAB para autocompletar
