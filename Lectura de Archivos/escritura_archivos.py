# escritura de archivos

# escribir archivos

archivo_estudiantes = open("estudiantes2.txt", "a")  # se crea un nuevo archivo txt automáticamente
print(archivo_estudiantes.write(
    "\nEsto es un nuevo archivo\n y podemos escribir con el codigo\n nuevas lineas de texto"))  # permiso de
# escritura, añadidura, etc.
# write
archivo_estudiantes.close()  # así cerramos un archivo
