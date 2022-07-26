# lectura de archivos(texto)

# abrir y cerrar archivos

archivo_estudiantes = open("estudiantes.txt", "r")  # así abrimos un archivo. con "r" lee, con "a" añade, con "w"
# crea uno nuevo y borra el contenido del anterior
for estudiantes in archivo_estudiantes:
    print(estudiantes)
print(archivo_estudiantes.readlines())  # read, readline, readlines
archivo_estudiantes.close()  # así cerramos un archivo
