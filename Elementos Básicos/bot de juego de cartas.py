# genera un bot de juego de cartas con una baraja de 52 cartas

import random
import sys
import time


# define la clase carta
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return str(self.numero) + " de " + self.palo


# define la clase baraja
class Baraja:
    def __init__(self):
        self.cartas = []
        for palo in ["oros", "copas", "bastos", "espadas"]:
            for numero in range(1, 14):
                self.cartas.append(Carta(numero, palo))

    def __str__(self):
        string_cartas = ""
        for carta in self.cartas:
            string_cartas += str(carta) + " "
        return string_cartas

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir(self, mano):
        if len(self.cartas) > 0:
            mano.recibir(self.cartas.pop())
        else:
            print("No hay cartas en la baraja")

    def repartir_cartas(self, manos):
        for mano in manos:
            self.repartir(mano)


# define la clase mano
class Mano:
    def __init__(self):
        self.cartas = []

    def recibir(self, carta):
        self.cartas.append(carta)

    def __str__(self):
        string_cartas = ""
        for carta in self.cartas:
            string_cartas += str(carta) + " "
        return string_cartas


# define la clase jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = Mano()

    def __str__(self):
        return self.nombre + " " + str(self.mano)


# define la clase mesa
class Mesa:
    def __init__(self):
        self.jugadores = []
        self.baraja = Baraja()
        self.baraja.barajar()

    def __str__(self):
        string_jugadores = ""
        for jugador in self.jugadores:
            string_jugadores += str(jugador) + " "
        return string_jugadores

    def repartir_cartas(self):
        self.baraja.repartir_cartas(self.jugadores)

    def mostrar_manos(self):
        for jugador in self.jugadores:
            print(jugador.nombre + ": " + str(jugador.mano))

    def jugar(self):
        for jugador in self.jugadores:
            print(jugador.nombre + ": " + str(jugador.mano))
            carta_jugada = int(input("¿Qué carta quieres jugar? "))
            while carta_jugada > len(jugador.mano.cartas) or carta_jugada < 1:
                print("Esa no es una carta válida")
                carta_jugada = int(input("¿Qué carta quieres jugar? "))
            carta_jugada = jugador.mano.cartas.pop(carta_jugada - 1)
            print(jugador.nombre + " ha jugado " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)

    def jugar_vs_cpu(self):
        for jugador in self.jugadores:
            print(jugador.nombre + ": " + str(jugador.mano))
            carta_jugada = int(input("¿Qué carta quieres jugar? "))
            while carta_jugada > len(jugador.mano.cartas) or carta_jugada < 1:
                print("Esa no es una carta válida")
                carta_jugada = int(input("¿Qué carta quieres jugar? "))
            carta_jugada = jugador.mano.cartas.pop(carta_jugada - 1)
            print(jugador.nombre + " ha jugado " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)
            print("CPU: " + str
            (self.jugadores[1].mano.cartas[0]))
            carta_jugada = self.jugadores[1].mano.cartas.pop(0)
            print("CPU ha jugado " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)

    # define la clase jugador_cpu


class Jugador_CPU(Jugador):
    def __init__(self, nombre):
        Jugador.__init__(self, nombre)

    def jugar(self):
        carta_jugada = self.mano.cartas.pop(0)
        print(self.nombre + " ha jugado " + str(carta_jugada))
        self.baraja.cartas.append(carta_jugada)
        self.baraja.barajar()
        self.baraja.repartir_cartas(self.jugadores)
        self.mostrar_manos()
        time.sleep(1)
        print("CPU: " + str
        (self.jugadores[1].mano.cartas[0]))
        carta_jugada = self.jugadores[1].mano.cartas.pop(0)
        print("CPU ha jugado " + str(carta_jugada))
        self.baraja.cartas.append(carta_jugada)
        self.baraja.barajar()
        self.baraja.repartir_cartas(self.jugadores)
        self.mostrar_manos()
        time.sleep(1)


# define la clase juego
class Juego:
    def __init__(self):
        self.mesa = Mesa()
        self.jugadores = []
        self.jugadores.append(Jugador("Jugador"))
        self.jugadores.append(Jugador_CPU("CPU"))
        self.mesa.jugadores = self.jugadores
        self.mesa.repartir_cartas()
        self.mesa.mostrar_manos()
        self.mesa.jugar()
        self.mesa.jugar_vs_cpu()


# define la clase carta
class Carta:
    def __init__(self, palo, numero):
        self.palo = palo
        self.numero = numero

    def __str__(self):
        return str(self.numero) + " de " + self.palo


# define la clase baraja
class Baraja:
    def __init__(self):
        self.cartas = []
        self.crear_baraja()

    def crear_baraja(self):
        for palo in ["oros", "copas", "bastos", "espadas"]:
            for numero in range(1, 14):
                self.cartas.append(Carta(palo, numero))

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir_cartas(self, jugadores):
        for jugador in jugadores:
            jugador.mano.cartas = self.cartas[:5]
            self.cartas = self.cartas[5:]


# define la clase mano
class Mano:
    def __init__(self):
        self.cartas = []

    def __str__(self):
        string_cartas = ""
        for carta in self.cartas:
            string_cartas += str(carta) + " "
        return string_cartas


# define la clase mesa
class Mesa:
    def __init__(self):
        self.jugadores = []

    def repartir_cartas(self):
        self.baraja.barajar()
        for jugador in self.jugadores:
            jugador.mano.cartas = self.baraja.cartas[:5]
            self.baraja.cartas = self.baraja.cartas[5:]

    def mostrar_manos(self):
        for jugador in self.jugadores:
            print(jugador.nombre + ": " + str(jugador.mano))

    def jugar(self):
        for jugador in self.jugadores:
            carta_
            print(jugador.nombre + "
            ha
            jugado
            " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)

    def jugar_vs_cpu(self):
        for jugador in self.jugadores:
            print(jugador.nombre + ": " + str(jugador.mano))
            carta_jugada = int(input("¿Qué carta quieres jugar? "))
            while carta_jugada > len(jugador.mano.cartas) or carta_jugada < 1:
                print("Esa no es una carta válida")
                carta_jugada = int(input("¿Qué carta quieres jugar? "))
            carta_jugada = jugador.mano.cartas.pop(carta_jugada - 1)
            print(jugador.nombre + " ha jugado " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)
            print("CPU: " + str
            (self.jugadores[1].mano.cartas[0]))
            carta_jugada = self.jugadores[1].mano.cartas.pop(0)
            print("CPU ha jugado " + str(carta_jugada))
            self.baraja.cartas.append(carta_jugada)
            self.baraja.barajar()
            self.baraja.repartir_cartas(self.jugadores)
            self.mostrar_manos()
            time.sleep(1)


# juega un numero de veces
juego = Juego()
juego.jugar()
juego.jugar_vs_cpu()

# termina el programa y se cierra
input("Pulse cualquier tecla para salir")
sys.exit()
