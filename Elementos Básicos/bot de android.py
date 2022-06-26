#crea un asitente que te ayude a usar el smartphone

def main():
    print("Hola, soy Jarvis, el bot de android")
    print("Para usarme, debes escribirme")
    print("Para salir, escribe 'salir'")
    while True:
        mensaje = input(">> ")
        if mensaje == "salir":
            break
        print("Hola, soy Jarvis, el bot de android")
        print("Para usarme, debes escribirme")
        print("Para salir, escribe 'salir'")
    print("Bienvenido al asistente de Android")
    print("Para comenzar, introduce tu nombre")
    nombre = input()
    print("Hola " + nombre + "!")
    print("Para comenzar, introduce tu edad")
    edad = int(input())
    print("Tu edad es " + str(edad))
    print("Para comenzar, introduce tu altura")
    altura = float(input())
    print("Tu altura es " + str(altura))
    print("Para comenzar, introduce tu peso")
    peso = float(input())
    print("Tu peso es " + str(peso))
    print("Para comenzar, introduce tu sexo")
    sexo = input()
    print("Tu sexo es " + str(sexo))
    print("Para comenzar, introduce tu color de ojos")
    color_ojos = input()
    print("Tu color de ojos es " + str(color_ojos))
    print("Para comenzar, introduce tu color de piel")
    color_piel = input()
    print("Tu color de piel es " + str(color_piel))
    print("Para comenzar, introduce tu color de pelo")
    color_pelo = input()
    
#define la clase android
class Android:
    def __init__(self, nombre, edad, altura, peso, sexo, color_ojos, color_piel, color_pelo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
        self.color_ojos = color_ojos
        self.color_piel = color_piel
        self.color_pelo = color_pelo
    def saludar(self):
        print("Hola, soy " + self.nombre)
        print("Mi edad es " + str(self.edad))
        print("Mi altura es " + str(self.altura))
        print("Mi peso es " + str(self.peso))
        print("Mi sexo es " + self.sexo)
        print("Mi color de ojos es " + self.color_ojos)
        print("Mi color de piel es " + self.color_piel)
        print("Mi color de pelo es " + self.color_pelo)
    def despedirse(self):   
        print("Hasta luego, " + self.nombre)

#crea un objeto de la clase android
android = Android("Jarvis", 20, 1.70, 70, "masculino", "azul", "blanco", "rubio")
android.saludar()
android.despedirse()

#crea un menu de opciones
def menu():
    print("Hola, soy Jarvis, el bot de android")
    print("Para usarme, debes escribirme")
    print("Para salir, escribe 'salir'")
    while True:
        mensaje = input(">> ")
        if mensaje == "salir":
            break
        print("Hola, soy Jarvis, el bot de android")
        print("Para usarme, debes escribirme")
        print("Para salir, escribe 'salir'")
    print("Bienvenido al asistente de Android")
    print("Para comenzar, introduce tu nombre")
    nombre = input()
    print("Hola " + nombre + "!")
    print("Para comenzar, introduce tu edad")
    edad = int(input())
    print("Tu edad es " + str(edad))
    print("Para comenzar, introduce tu altura")
    altura = float(input())
    print("Tu altura es " + str(altura))
    print("Para comenzar, introduce tu peso")
    peso = float(input())
    print("Tu peso es " + str(peso))
    print("Para comenzar, introduce tu sexo")
    sexo = input()
    print("Tu sexo es " + str(sexo))
    print("Para comenzar, introduce tu color de ojos")
    color_ojos = input()
    print("Tu color de ojos es " + str(color_ojos))
    print("Para comenzar, introduce tu color de piel")
    color_piel = input()
    print("Tu color de piel es " + str(color_piel))
    print("Para comenzar, introduce tu color de pelo")
    color_pelo = input()
    android = Android(nombre, edad, altura, peso, sexo, color_ojos, color_piel, color_pelo)
    android.saludar()
    android.despedirse()

#llama a la función menu
menu()

#ejecuta el programa
if __name__ == "__main__":
    main()
    
#cerramos el programa
print("Gracias por usarme")
print("Adios!")

    
#fin de la clase android


