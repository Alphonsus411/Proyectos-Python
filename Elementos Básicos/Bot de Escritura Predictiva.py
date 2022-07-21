# crea un programa de escritura predictiva que lee un texto y lo completa en base al texto leído.
# El programa debe leer un archivo de texto y completarlo con el texto leído
# el programa debe almacenar el texto completado en un archivo de texto
# el programa debe mostrar el texto completado en pantalla
# el programa debe ir mostrando varias opciones al usuario
# el programa debe permitir al usuario elegir una opción
# el programa debe permitir al usuario elegir una palabra para reemplazar
# el programa debe permitir escoger un texto para reemplazar
# el programa debe ir escribiendo el texto completado en el archivo de texto

escritura = open("escritura.txt", "w")
escritura.write("")
escritura.close()

# leer el archivo de texto
escritura = open("escritura.txt", "r")
texto = escritura.read()
escritura.close()

# escribir el archivo de texto
escritura = open("escritura.txt", "w")
escritura.write(texto)
escritura.close()

# almacenar el texto completado en un archivo de texto
escritura = open("escritura.txt", "r")
escritura = escritura.read()

# mostrar el texto completado en pantalla
print(escritura)

# opciones del programa
print("1. Reemplazar una palabra")
print("2. Reemplazar un texto")
print("3. Salir")

# elegir una opcion
opcion = int(input("Elige una opcion: "))

# reemplazar una palabra
if opcion == 1:
    palabra = input("Escribe la palabra que quieres reemplazar: ")
    reemplazo = input("Escribe la palabra que quieres reemplazarla: ")
    escritura = open("escritura.txt", "r")
    escritura = escritura.read()
    escritura = escritura.replace(palabra, reemplazo)
    escritura = open("escritura.txt", "w")
    escritura.write(escritura)  # escribe el texto en el archivo
    escritura.close()
    escritura = open("escritura.txt", "r")
    escritura = escritura.read()
    print(escritura)

# reemplazar un texto
if opcion == 2:
    texto = input("Escribe el texto que quieres reemplazar: ")
    reemplazo = input("Escribe el texto que quieres reemplazarlo: ")
    escritura = open("escritura.txt", "r")
    escritura = escritura.read()
    escritura = escritura.replace(texto, reemplazo)
    escritura = open("escritura.txt", "w")
    escritura.write(escritura)
    escritura.close()
    escritura = open("escritura.txt", "r")
    escritura = escritura.read()
    print(escritura)

# salir del programa
if opcion == 3:
    print("Gracias por usar el programa")
    exit()

# si el usuario no elige una opcion valida
if opcion != 1 and opcion != 2 and opcion != 3:
    print("Elige una opcion valida")
    exit()

# cerrar el archivo de texto
escritura.close()
lectura.close()

# mensaje de despedida
print("Gracias por usar el programa")
