# 🧠 Simulación del flujo de Git
# Working Directory → Staging → Repository

print("📁 Working Directory (archivos modificados)")

# Simulamos cambios en archivos
archivo = "app.py"
print(f"✏️ Modificando archivo: {archivo}")

# Paso 1: git add
print("\n➡️ Ejecutando: git add app.py")
print("📦 Archivo agregado al Staging Area")

# Paso 2: git commit
print("\n➡️ Ejecutando: git commit -m 'feat: add new feature'")
print("📸 Commit creado (snapshot guardado)")

# Estado final
print("\n✅ Archivo ahora está guardado en el Repository")
