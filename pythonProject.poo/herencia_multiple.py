# herencia_multiple

class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("llamando....")

    def ocupado(self):
        print("ocupado...")


class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print("tomando fotos...")


class Reproductor:
    def __init__(self):
        pass

    def reproductor_musica(self):
        print("reproduciendo musica")

    def reproducir_video(self):
        print("reproduciendo video...")


class Smartphone(Telefono, Camara, Reproductor):
    def __del__(self):  # limpia los metodos vacíos y ayuda a llamar a las subclases
        print("telefono apagado")


movil = Smartphone()

# print(dir(movil)) #genera un listado con los métodos que pueden introducirse en el objeto para trabajar con él

print(movil.llamar())





