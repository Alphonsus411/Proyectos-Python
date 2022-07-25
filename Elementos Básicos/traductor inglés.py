# crea un programa de traducción de inglés a español
# autor: @eymard

def traductor_ingles():
    print("""
    El traductor de inglés a español
    """)
    print("""
    1. Ingles a Español
    2. Español a Ingles
    3. Salir
    """)
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        ingles_espanol()
    elif opcion == 2:
        espanol_ingles()
    elif opcion == 3:
        print("Adiós")
    else:
        print("Opción incorrecta")
        traductor_ingles()


# ingles a español
def ingles_espanol():
    print("""
    El traductor de inglés a español
    """)
    ingles = input("Inglés: ")
    ingles = ingles.lower()
    if ingles == "hello":
        print("Hola")
    elif ingles == "how are you":
        print("Cómo estás")
    elif ingles == "goodbye":
        print("Adiós")
    elif ingles == "bye":
        print("Adiós")
    elif ingles == "good morning":
        print("Buenos días")
    elif ingles == "good afternoon":
        print("Buenas tardes")
    elif ingles == "good evening":
        print("Buenas noches")
    elif ingles == "good night":
        print("Buenas noches")
    elif ingles == "how are you doing":
        print("Cómo estás")
    elif ingles == "how are you doing today":
        print("Cómo estás hoy")
    elif ingles == "what are you doing":
        print("Qué estás haciendo")
    elif ingles == "what are you doing today":
        print("Qué estás haciendo hoy")
    elif ingles == "what is your name":
        print("Cuál es tu nombre")
    elif ingles == "what are you from?":
        print("De dónde eres?")
    elif ingles == "good":
        print("Bien")
    elif ingles == "bad":
        print("Mal")
    elif ingles == "fine":
        print("Bien")
    elif ingles == "ok":
        print("Ok")
    elif ingles == "okay":
        print("Ok")
    elif ingles == "no":
        print("No")
