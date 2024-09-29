# Crear un Diccionario
informacion_personal = {
    "nombre": "David Loya",
    "edad": 39,
    "ciudad": "Quevedo",
    "profesion": "Mecanico"
}

# Acceder y Modificar Valores
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Sangolqui"  # Modificar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor
informacion_personal["profesion"] = "Servidor publico"  # Modificar la profesión
print("Profesión actualizada:", informacion_personal["profesion"])

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "098222484"  # Agregar número de teléfono ficticio

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el Diccionario Final
print("Información Personal Final:", informacion_personal)
