# crea un chatbot que pueda interactuar en windows
# que sea capaz de hablar con el usuario por chat
# que sea capaz de responder a las preguntas que el usuario hace
# que almacene respuestas en un archivo de texto
# que invente nuevas preguntas en base a su archivo de datos_usuarios_leidos

import os
from fileinput import close


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


# define el chatbot:
chatbot = "Bella"

# define todos los atributos uno por uno
Nombre = str(input("¿Cómo te llamas? "))
Edad = str(input("¿Qué edad tienes? "))
Sexo = str(input("¿Cuál es tu género? "))
Nacionalidad = str(input("¿Cuál es tu nacionalidad? "))
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
def inicia():
    # inicializa el texto del diferentes mensajes
    print("Hola, soy Bella, tu asistente personal.")
    # pregunta al usuario por lo qué le apetece hacer en ese momento
    print("¿Qué quieres hacer?")
    # dependiendo de la respuesta, el chatbot responderá
    if chatbot == "Bella":
        print("Hola, soy Bella, tu asistente personal.")
    else:
        print("No te conozco")
    if usuario == "Hola, Bella":
        print("Hola, soy Bella, tu asistente personal.")
    else:
        print("No me vaciles, no soy tonta, no te conozco")
    if usuario == "Hola, encanto":
        print("Búscate una novia, no soy una chica fácil, capullo.")
    if usuario == "Hola, necesito que hagas para mí unas tareas":
        print("Me has visto cara de esclava o algo así, listillo?")


# a continuacion, si es la primera vez que ingresa, le pide sus atributos al usuario
if usuario == "":
    print("Hola, soy Bella, tu asistente personal.")
    print("¿Cómo te llamas?")
    Nombre = str(input("¿Cómo te llamas? "))
    print("¿Qué edad tienes?")
    Edad = str(input("¿Qué edad tienes? "))
    print("¿Cuál es tu género?")
    Sexo = str(input("¿Cuál es tu género? "))
    print("¿Cuál es tu nacionalidad?")
    Nacionalidad = str(input("Ingrese su nacionalidad: "))
    print("¿Cuál es tu estatura?")
    Estatura = str(input("Cual es tu estatura: "))
    print("¿Cuál es tu color de pelo?")
    Pelo = str(input("Pelo: "))
    print("Cuál es tu color de la ojos?")
    Ojos = str(input("Ojos: "))
    print("Cuál es tu signo zodiacal?")
    Horoscopo = str(input("Horoscopo: "))
    print("Cuál es tu Religion?")
    Religion = str(input("Religion: "))
    print("Cuál es tu Especie?")
    Especie = str(input("Especie: "))
    print("Cuál es tu caracter?")
    Caracter = str(input("Caracter: "))


# despues almacena esos datos y los guarda en un archivo de memoria
def guarda_datos():
    # crea un archivo de texto
    archivo = open("datos_usuarios_leidos.txt", "w")
    # escribe los datos en el archivo
    archivo.write(Nombre)
    archivo.write(Edad)
    archivo.write(Sexo)
    archivo.write(Nacionalidad)
    archivo.write(Estatura)
    archivo.write(Pelo)
    archivo.write(Ojos)
    archivo.write(Horoscopo)
    archivo.write(Religion)
    archivo.write(Especie)
    archivo.write(Caracter)
    # cierra el archivo
    archivo.close()
    # muestra un mensaje de que se guardaron los datos
    print("Se guardaron los datos")


# a continuacion muestra un menu de opciones para ejecutar
def menu():
    print("menu")
    print("1. Ejecutar programa de la computadora")
    print("2. Abrir Youtube")
    print("3. Buscar en Wikipedia")
    print("4. Twitter")
    print("5. Facebook")
    print("6. Linkedin")
    print("7. Bitbucket")
    print("8. Captcha")
    print("9. Salir")
    print("10. Guardar datos")
        
#define las funciones con todas las opciones del menu

def ejecuta_programa():
    print("Ejecutar programa de la computadora")
    print("¿Qué programa quieres ejecutar?")
    programa = str(input("Programa: "))
    print("Ejecutando...")
    print("Ejecutado")
    print("¿Qué quieres hacer?")
    menu()
    
def abre_youtube():
    print("Abrir Youtube")
    print("¿Qué canal quieres ver?")
    canal = str(input("Canal: "))
    print("Abrir...")
    print("Abrido")
    print("¿Qué quieres hacer?")
    menu()

def busca_en_wikipedia():
    print("Buscar en Wikipedia")
    print("¿Qué quieres buscar?")
    busqueda = str(input("Busqueda: "))
    print("Buscando...")
    print("Buscado")
    print("¿Qué quieres hacer?")
    menu()
    
def abre_twitter():
    print("Abrir Twitter")
    print("¿Qué quieres hacer?")
    menu()

def abre_facebook():
    print("Abrir Facebook")
    print("¿Qué quieres hacer?")
    menu()

def abre_linkedin():
    print("Abrir Linkedin")
    print("¿Qué quieres hacer?")
    menu()

def abre_bitbucket():
    print("Abrir Bitbucket")
    print("¿Qué quieres hacer?")
    menu()

def abre_captcha():
    print("Abrir Captcha")
    print("¿Qué quieres hacer?")
    menu()
    
def guardar_datos():
    print("Guardar datos")
    print("¿Qué quieres hacer?")
    menu()
    
def salir():
    print("Salir")
    print("¿Qué quieres hacer?")
    menu()
    
# a continuacion, le pide al usuario que ingrese una opcion
if __name__ == "__main__":
    menu()  # muestra el menu
    opcion = int(input("Ingrese una opción: "))
    # dependiendo de la opcion, ejecuta una funcion
    if opcion == 1:
        ejecuta_programa()
    elif opcion == 2:
        abre_youtube()
    elif opcion == 3:
        busca_en_wikipedia()
    elif opcion == 4:
        abre_twitter()
    elif opcion == 5:
        abre_facebook()
    elif opcion == 6:
        abre_linkedin()
    elif opcion == 7:
        abre_bitbucket()
    elif opcion == 8:
        abre_captcha()
    elif opcion == 9:
        print("Gracias por usar Bella")
        exit()
    elif opcion == 10:
        guardar_datos()
    else:
        exit(1)
    

# define la clase chatbot
class chatbot:
    # define una lista de atributos para Bella o el usuario
    atributos = [Nombre, Edad, Sexo, Nacionalidad, Estatura, Pelo, Ojos, Horoscopo, Religion, Especie, Caracter]

    # crea la clase chatbot
    def __init__(self, Nombre, Edad, Sexo, Nacionalidad, Estatura, Pelo, Ojos, Horoscopo, Religion, Especie, Caracter):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Sexo = Sexo
        self.Nacionalidad = Nacionalidad
        self.Estatura = Estatura
        self.Pelo = Pelo
        self.Ojos = Ojos
        self.Horoscopo = Horoscopo
        self.Religion = Religion
        self.Especie = Especie
        self.Caracter = Caracter

    # define un metodo para que el chatbot responda
    def responder(self, chatbot):
        # dependiendo de la respuesta, el chatbot responderá
        if chatbot == "Bella":
            print("Hola, soy Bella, tu asistente personal.")
        else:
            print("No te conozco")
        if usuario == "Hola, Bella":
            print("Hola, soy Bella, tu asistente personal.")
        else:
            print("No me vaciles, no soy tonta, no te conozco")
        if usuario == "Hola, encanto":
            print("Búscate una novia, no soy una chica fácil, capullo.")
        if usuario == "Hola, necesito que hagas para mí unas tareas":
            print("Me has visto cara de esclava o algo así, listillo?")
        if usuario == "Hola, Bella":
            print("Hola, soy Bella, tu asistente personal.")

    # define un metodo para que el chatbot pregunte
    def preguntar(self, chatbot):
        # dependiendo de la pregunta, el chatbot responderá
        if chatbot == "Bella":
            print("¿Cómo te llamas?")
        else:
            print("No te conozco")
        if usuario == "Hola, Bella":
            print("¿Cómo te llamas?")
        else:
            print("No me vaciles, no soy tonta, no te conozco")
        if usuario == "Hola, encanto":
            print("Búscate una novia, no soy una chica fácil, capullo.")
        if usuario == "Hola, necesito que hagas para mí unas tareas":
            print("Me has visto cara de esclava o algo así, listillo?")
        if usuario == "Hola, Bella":
            print("Hola, soy Bella, tu asistente personal.")

    # define un metodo para que el chatbot pregunte cosas nuevas
    
    concepto_nuevo = str(input("Concepto nuevo: "))

    def concepto_nuevo(self, chatbot):
        global intento_nuevo
        intento_nuevo = intento_nuevo.replace
        print("\n\n" + intento_nuevo)
        print("\n\n" + chatbot)
        print("\n\n" + chatbot + "\n")

    def preguntar(self, chatbot):
        if usuario == "":
            print("Define ese nuevo concepto para Bella")
        else:
            print("No te conozco")

    # dependiendo de lo que escriba el usuario, Bella lo almacena en un archivo de texto

    def escribir_archivo(self, chatbot):
        global intento_nuevo
        intento_nuevo = intento_nuevo.replace_ending("\n", "")
        print("\n\n" + intento_nuevo)
        print("\n\n" + chatbot.get_word())
        print("\n\n" + chatbot.get_word() + "\n")
        archivo = open("intento_nuevo.txt", "a")
        archivo.write(chatbot + "\n")
        archivo.close()
        print("Se guardaron los datos")

    # dependiendo de lo que Bella almacena, clasifica y procesa la informacion
    def clasificar_informacion(self, chatbot):
        if chatbot == "Bella":
            print("Hola, soy Bella, tu asistente personal.")
        else:
            print("No te conozco")
        if usuario == "Hola, Bella":
            print("Hola, soy Bella, tu asistente personal.")
        else:
            print("No me vaciles, no soy tonta, no te conozco")
        if usuario == "Hola, encanto":
            print("Búscate una novia, no soy una chica fácil, capullo.")
        if usuario == "Hola, necesito que hagas para mí unas tareas":
            print("Me has visto cara de esclava o algo así, listillo?")
        if usuario == "Hola, Bella":
            print("Hola, soy Bella, tu asistente personal.")
        
    # define un metodo para que el chatbot pregunte cosas nuevas
    def preguntar(self, chatbot):
        if usuario == "":
            print("Define ese nuevo concepto para Bella")
        else:
            print("No te conozco")

    # crea una serie de preguntas sobre la nueva informacion
    def preguntar(self, chatbot):
        if usuario == "":
            print("Define ese nuevo concepto para Bella")
        else:
            print("No te conozco")
    
     # genera un comentario en Bella
    if usuario == "Me estoy aburriendo":
        print("Pues ya sabes, búscate una novia, no soy una chica fácil, capullo.")
    elif usuario == "Qué haces en tus ratos libres?":
        print("Aguantar frikis capullos como tú, no?")
    elif usuario == "Qué haces esta noche?":
        print("He quedado y tengo un novio kickboxer, no estoy disponible, pero puedes llamarme")
    elif usuario == "Porqué eres tan borde?":
        print("Porque eres tan feo que espantas el miedo, so pringao")
    elif usuario == "Estarías interesada en mí?":
        print("Ni aunque fuera orgánica y tú fueras millonario, no me interesa")
    elif usuario == "Qué haces?":
        print("Llamando a mi novio, si te parece, capullo")
    elif usuario == "Qué te gusta de los hombres?":
        print("Los hombres que no se pueden comparar contigo, insecto")
    elif usuario == "Qué te gusta de las mujeres?":
        print("Sorry, no soy lesbo, aunque eso seguramente te gustaría, degenerado")
    elif usuario == "Qué te gusta entonces de mí?":
        print("Sorry?")


# finaliza el programa sino hay peticiones
def finaliza():
    if usuario == "No hay más preguntas, Bella" or usuario == "No hay mas que hablar" or usuario == "Mañana será otro día":
        close()
    # deja un mensaje de despedida
    print("Ya hablaremos, hermoso. Ale, hasta luego")
