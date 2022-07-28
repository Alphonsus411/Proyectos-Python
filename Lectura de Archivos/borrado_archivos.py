# escritura de archivos

# escribir archivos

archivo_estudiantes = open("estudiantes2.txt", "a")  # se crea un nuevo archivo txt automáticamente
print(archivo_estudiantes.write(
    "\nEsto es un nuevo archivo\n y podemos escribir con el codigo\n nuevas lineas de texto"))
archivo_estudiantes.close()  # así cerramos un archivo

# eliminar un archivo

import os  # libreria específica para funcionalidades de sistema operativo, como borrado y eliminación

os.remove("estudiantes2.txt")
