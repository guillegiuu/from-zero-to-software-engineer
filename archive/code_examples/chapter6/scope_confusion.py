# scope_confusion.py
# Error común: creer que una variable local cambia la variable global

mensaje = "Hola desde afuera"

def cambiar_mensaje():
    mensaje = "Hola desde adentro"
    print("Dentro de la función:", mensaje)

cambiar_mensaje()

print("Fuera de la función:", mensaje)
