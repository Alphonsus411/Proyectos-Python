                                                                                                                                            #crea un chatbot femenino que responde a preguntas y haga comentarios sexys
#que pueda buscar en internet datos
#que aprenda de los conceptos expuestos
#que tenga una base de datos 
#que sea capaz de almacenar los datos y relacionarlos
#que tenga personalidad

import os
from fileinput import close
from tkinter import Menu


class Bella:
    Nombre = "Bella"
    Edad = "30"
    Sexo = "Femenino"
    Nacionalidad = "Española"
    Estatura = "1.70"
    Pelo = "Pelirrojo"
    Ojos = "Verdes"
    Horoscopo = "Escorpion"
    Religion = "Budista"
    Especie = "Chatbot"
    Caracter = "Ironico"


#define el chatbot
chatbot = "Bella"

# define todos los atributos uno por uno
Nombre = str(input("Introduce tu nombre de  forma correcta: "))
Edad = str(input("¿Cuántos años de edad tienes? "))
Sexo = str(input("¿Cuál es tu género? "))
Nacionalidad = str(input("¿Cuál es tu procedencia? "))
Estatura = str(input("¿Cuánto mides? "))
Pelo = str(input("¿Cuál es tu color de pelo? "))
Ojos = str(input("¿Cuál es tu color de ojos? "))
Horoscopo = str(input("¿Cuál es tu signo zodiacal? "))
Religion = str(input("Cuál es tu religion? "))
Especie = str(input("¿Cuál es tu especie? "))
Caracter = str(input("Cuál es tu caracter? "))

# define una lista de atributos para Bella o el usuario
atributos = [Nombre, Edad, Sexo, Nacionalidad, Estatura, Pelo, Ojos, Horoscopo, Religion, Especie, Caracter]


# crea la clase usuario
class usuario:
    Nombre = ""
    Edad = ""
    Sexo = ""
    Nacionalidad = ""
    Estatura = ""
    Pelo = ""
    Ojos = ""
    Horoscopo = ""
    Religion = ""
    Especie = ""
    Caracter = ""


# inicia el programa con un saludo

print("Hola, soy " + chatbot + " y estoy aquí para ayudarte")
print("¿Qué quieres hacer?")
Menu()
menu = Menu()

#define el menu
def menu():
    print("1. Preguntar")
    print("2. Comentar")
    print("3. Salir")
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        preguntar()
    elif opcion == 2:
        comentar()
    elif opcion == 3:
        print("Hasta pronto")
        exit()
    else:
        print("Opción incorrecta")
        menu()

#define la pregunta
def preguntar():
    print("¿Qué quieres saber?")
    pregunta = str(input("Introduce una pregunta: "))
    print("¿" + pregunta + "?")
    menu()
    
#define el comentario
def comentar():
    print("Qué me habías comentado antes?")
    comentario = str(input("Introduce un comentario: "))
    print("¡Gracias por" + comentario + "!")
    
    #define la respuesta
    print("¿Qué quieres saber?")
    respuesta = str(input("Introduce una pregunta: "))
    print("¿" + respuesta + "?")
    
#crea una lista de comentarios en base a conversaciones
lista_de_comentarios = []

#crea una lista de preguntas en base a conversaciones
lista_de_preguntas = []

#crea una base de datos con los comentarios y preguntas
def base_de_datos():
    lista_de_comentarios.append(comentario)
    lista_de_preguntas.append(pregunta)
    print("¡Gracias por tu comentario!")
    menu()
    
comentario = str(input("Introduce un comentario: "))
pregunta = str(input("Introduce una pregunta: "))

#crea una base de datos para Bella en formato csv
def base_de_datos_csv():
    with open('base_de_datos.csv', 'w') as f:
        f.write(str(lista_de_comentarios))
        f.write(str(lista_de_preguntas))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos para Bella en formato txt
def base_de_datos_txt():
    with open('base_de_datos.txt', 'w') as f:
        f.write(str(lista_de_comentarios))
        f.write(str(lista_de_preguntas))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos para Bella en formato json
def base_de_datos_json():
    with open('base_de_datos.json', 'w') as f:
        f.write(str(lista_de_comentarios))
        f.write(str(lista_de_preguntas))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos para Bella en formato xml
def base_de_datos_xml():
    with open('base_de_datos.xml', 'w') as f:
        f.write(str(lista_de_comentarios))
        f.write(str(lista_de_preguntas))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos para Bella en formato html
def base_de_datos_html():
    with open('base_de_datos.html', 'w') as f:
        f.write(str(lista_de_comentarios))
        f.write(str(lista_de_preguntas))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos que una lista de atributos
def base_de_datos_lista():
    with open('base_de_datos.txt', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos que una lista de atributos
def base_de_datos_lista_csv():
    with open('base_de_datos.csv', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos que una lista de atributos
def base_de_datos_lista_json():
    with open('base_de_datos.json', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos que una lista de atributos
def base_de_datos_lista_xml():
    with open('base_de_datos.xml', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()

#crea una base de datos que una lista de atributos
def base_de_datos_lista_html():
    with open('base_de_datos.html', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()
        
#crea una base de datos que una lista de atributos
def base_de_datos_lista_txt():
    with open('base_de_datos.txt', 'w') as f:
        f.write(str(atributos))
        f.close()
        print("¡Gracias por tu comentario!")
        menu()
    
#almecenar los atributos en el PC
def almacenar_atributos():
    print("¿Qué quieres almacenar?")
    atributo = str(input("Introduce un atributo: "))
    print("¡Gracias por tu comentario!")
    atributos.append(atributo)
    menu()

#cuando Bella permanece un tiempo inactiva, cierra el programa
def cerrar_programa():
    print("¡Hasta pronto!")
    exit()
    





