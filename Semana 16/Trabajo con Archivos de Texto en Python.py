# Escritura de Archivo de Texto
# Se crea un nuevo archivo llamado my_notes.txt y se escriben algunas notas.

# Abrimos el archivo en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Este es un deber de la sema 16.\n")
    file.write("hoy aremos un archivo Python.\n")
    file.write("Seguiremos mejorando el aprendizaje.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Utilizamos strip() para eliminar saltos de línea al final

# No es necesario cerrar el archivo explícitamente, ya que usamos 'with',
# que lo cierra automáticamente al salir del bloque.
