# Juego de Cartas "Orden":

from ast import Call
from tkinter import Tk


class juego:
    def __init__(self):
        self.cartas = ['A1', 'A26', 'B2', 'B25', 'C3', 'C24', 'D4', 'D23', 'E5', 'E22', 'F6', 'F21', 'G7', 'G20', 'H8', 'H19', 'I9', 'I18', 'J10', 'J17', 'K11', 'K16', 'L12', 'L15', 'M13', 'M14', 'N14', 'N13', 'O15', 'O12', 'P16', 'P11', 'Q17', 'Q10', 'R18', 'R9', 'S19', 'S8', 'T20', 'T7', 'U21', 'U6', 'V22', 'V5', 'W23', 'W4', 'X24', 'X3', 'Y25', 'Y2', 'Z26', 'Z1']
        self.letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
    
# Consiste en una baraja con letras del abecedario y números, cada valor en un extremo de la carta.

    def baraja(self):
        return self.cartas

    def letras(self):
        return self.letras
    
    def numeros(self):
        return self.numeros

    def baraja_aleatoria(self):
        import random
        random.shuffle(self.cartas)
        return self.cartas
    
    def baraja_aleatoria_letras(self):
        import random
        random.shuffle(self.letras)
        return self.letras
    
    def baraja_aleatoria_numeros(self):
        import random
        random.shuffle(self.numeros)
        return self.numeros
    
    def baraja_aleatoria_letras_numeros(self):
        import random
        random.shuffle(self.letras)
        random.shuffle(self.numeros)
        return self.letras, self.numeros
    
    def baraja_aleatoria_numeros_letras(self):
        import random
        random.shuffle(self.numeros)
        random.shuffle(self.letras)
        return self.numeros, self.letras

# 1. La mecánica del juego es sencilla: hay que quedarse sin cartas lo antes posible dejándolas por orden (alfabético o numérico) en la mesa, ya sea ascendente o descendente.
    def mecanica(self):
        if self.cartas == self.cartas:
            return True
        else:
            return False

# 2. Al comienzo de la partida, se mezcla la baraja y se dan seis o siete cartas a cada participante.
    def mezcla(self):
        import random
        random.shuffle(self.cartas)
        return self.cartas[:6]

    def mezcla_letras(self):
        import random
        random.shuffle(self.letras)
        return self.letras[:6]
    
    def mezcla_numeros(self):
        import random
        random.shuffle(self.numeros)
        return self.numeros[:6]
    
    def mezcla_letras_numeros(self):
        import random
        random.shuffle(self.letras)
        random.shuffle(self.numeros)
        return self.letras[:6], self.numeros[:6]

# Cada turno un jugador roba una carta del mazo, hasta que al final no queden cartas en la baraja.
    def roba(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
    
    def roba_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def roba_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def roba_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        

# 3. El turno de ronda va en sentido horario o anti horario. Cada jugador debe dejar sobre la mesa (si puede) una carta que sea la continuidad (ascendente o descendente) de la anterior. Es como jugar un "solitario".
    def turno(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def turno_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def turno_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def turno_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()


# 4. Cada vez que se completa una vuelta, el último jugador puede decidir "hacia arriba o hacia abajo" y cambiar el orden de continuidad.

    def vuelta(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def vuelta_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def vuelta_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def vuelta_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        

# 5. El jugador que se queda sin cartas dice "fiesta" al final de su ronda y gana la partida.

    def fiesta(self):
        if self.cartas == []:
            return True
        else:
            return False
        
    def fiesta_letras(self):
        if self.letras == []:
            return True
        else:
            return False
        
    def fiesta_numeros(self):
        if self.numeros == []:
            return True
        else:
            return False

# 6. El juego no tiene máximo de mesa, cuando se llegue el máximo del ancho de la mesa se puede poner arriba o abajo, formando una hilera, en la nueva hilera se puede empezar por donde se quiera, no es obligado por los extremos.

    def hilera(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def hilera_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
    
    def hilera_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def hilera_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        
# 7. Para empezar el juego cada jugador levanta la carta de arriba y el número más alto empieza.

    def empieza(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def empieza_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def empieza_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def empieza_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        

# 8. Si no puedes poner una carta en mesa, debes robar como penalización, aunque robes, no puedes jugar la carta robada, ya que es una penalización.

    def penalizacion(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def penalizacion_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def penalizacion_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def penalizacion_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
          

# 9. La mano no tiene límite de cartas.
    def mano(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()

# 10. Cuando se empieza la partida se puede iniciar poniendo las carta en el medio, las hileras siguientes podrás empezarlas por donde se quiera, pero si empiezas por el extremo, se puede colocar cartas por el otro extremo con la regla de izquierda y derecha.
    def inicio(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def inicio_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def inicio_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def inicio_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        
# 11. Si el juego se atasca, hay 2 soluciones:

    def atascado(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
# -	Se empieza una hilera nueva por donde se quiera y se rompe el orden
    def atascado_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
    
    def atascado_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
    
    def atascado_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
          
# -	Gana el jugador con menos cartas en mano.

    def atascado_ganador(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def atascado_ganador_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def atascado_ganador_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def atascado_ganador_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        

# 12.Cada hilera va a tener un máximo de 11 cartas seguidas y un máximo de 5 hileras

    def hilera_max(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def hilera_max_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def hilera_max_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
    
    def hilera_max_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        
# 13. Uso de Carta “Cuenta”: habrá una carta que finaliza completamente la partida, y sólo puede usarse en el turno activo del jugador. Éste naipe introduce la regla de terminar el juego haciendo que todos los jugadores cuenten su mano, de forma que, el que menos cartas tenga, gana esta ronda. Sólo hay cinco copias de esta carta especial en toda la baraja.
    def cuenta(self):
        if self.cartas == []:
            return False
        else:
            return self.cartas.pop()
        
    def cuenta_letras(self):
        if self.letras == []:
            return False
        else:
            return self.letras.pop()
        
    def cuenta_numeros(self):
        if self.numeros == []:
            return False
        else:
            return self.numeros.pop()
        
    def cuenta_letras_numeros(self):
        if self.letras == [] and self.numeros == []:
            return False
        else:
            return self.letras.pop(), self.numeros.pop()
        
class jugador:
    def __init__(self, nombre, mano, puntos):
        self.nombre = nombre
        self.mano = mano
        self.puntos = puntos
        
    def __str__(self):
        return self.nombre + " " + str(self.mano) + " " + str(self.puntos)
    
    def __repr__(self):
        return self.nombre + " " + str(self.mano) + " " + str(self.puntos)
    
    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __hash__(self):
        return hash(self.nombre)
    
    def __lt__(self, other):
        return self.puntos < other.puntos
    
    def __gt__(self, other):
        return self.puntos > other.puntos
    
    def __le__(self, other):
        return self.puntos <= other.puntos
    
    def __ge__(self, other):
        return self.puntos >= other.puntos
    
    def __ne__(self, other):
        return self.nombre != other.nombre
    
    def __add__(self, other):
        return self.puntos + other.puntos
    
    def __sub__(self, other):
        return self.puntos - other.puntos
    
    def __mul__(self, other):
        return self.puntos * other.puntos
    
    def __truediv__(self, other):
        return self.puntos / other.puntos
    
    def __floordiv__(self, other):
        return self.puntos // other.puntos
    
    def __mod__(self, other):
        return self.puntos % other.puntos
    
    def __divmod__(self, other):
        return divmod(self.puntos, other.puntos)

    def __pow__(self, other):
        return self.puntos ** other.puntos
    
    def __lshift__(self, other):
        return self.puntos << other.puntos
    
    def __rshift__(self, other):
        return self.puntos >> other.puntos
    
    def __and__(self, other):
        return self.puntos & other.puntos
    
    def __xor__(self, other):
        return self.puntos ^ other.puntos
    
    def __or__(self, other):
        return self.puntos | other.puntos
    
    def __radd__(self, other):
        return self.puntos + other.puntos
    
    def __rsub__(self, other):
        return self.puntos - other.puntos
    
    def __rmul__(self, other):
        return self.puntos * other.puntos
    
    def __rtruediv__(self, other):
        return self.puntos / other.puntos
    
    def __rfloordiv__(self, other):
        return self.puntos // other.puntos
    
    def __rmod__(self, other):
        return self.puntos % other.puntos
    
    def __rdivmod__(self, other):
        return divmod(self.puntos, other.puntos)
    
    def __rpow__(self, other):
        return self.puntos ** other.puntos
    
    def __rlshift__(self, other):
        return self.puntos << other.puntos
    
    def __rrshift__(self, other):
        return self.puntos >> other.puntos
    
    def __rand__(self, other):
        return self.puntos & other.puntos
    
    def __rxor__(self, other):
        return self.puntos ^ other.puntos
    
    def __ror__(self, other):
        return self.puntos | other.puntos
    
    def __iadd__(self, other):
        self.puntos += other.puntos
        return self.puntos
    
    def __isub__(self, other):
        self.puntos -= other.puntos
        return self.puntos
    
    def __imul__(self, other):
        self.puntos *= other.puntos
        return self.puntos
    
    def __itruediv__(self, other):
        self.puntos /= other.puntos
        return self.puntos
    
    def __ifloordiv__(self, other):
        self.puntos //= other.puntos
        return self.puntos
    
    def __imod__(self, other):
        self.puntos %= other.puntos
        return self.puntos
    
    def __ipow__(self, other):
        self.puntos **= other.puntos
        return self.puntos
    
    def __ilshift__(self, other):
        self.puntos <<= other.puntos
        return self.puntos
    
    def __irshift__(self, other):
        self.puntos >>= other.puntos
        return self.puntos
    
    def __iand__(self, other):
        self.puntos &= other.puntos
        return self.puntos
    
    def __ixor__(self, other):
        self.puntos ^= other.puntos
        return self.puntos
    
    def __ior__(self, other):
        self.puntos |= other.puntos
        return self.puntos
    
    def __neg__(self):
        return -self.puntos

    def __pos__(self):
        return +self.puntos
    
    def __abs__(self):
        return abs(self.puntos)
    
    def __invert__(self):
        return ~self.puntos
    
    def __complex__(self):
        return complex(self.puntos)
    
    def __int__(self):
        return int(self.puntos)
    
    def __float__(self):
        return float(self.puntos)
    
    def __oct__(self):
        return oct(self.puntos)
    
    def __hex__(self):
        return hex(self.puntos)

    def __index__(self):
        return self.puntos.__index__()
    
    def __coerce__(self, other):
        return self.puntos.__coerce__(other)
    
    def __enter__(self):
        return self.puntos.__enter__()
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.puntos.__exit__(exc_type, exc_value, traceback)
    
    def __trunc__(self):
        return self.puntos.__trunc__()
    
    def __round__(self, n=0):
        return self.puntos.__round__(n)
    
    def __ceil__(self):
        return self.puntos.__ceil__()
    
    def __floor__(self):
        return self.puntos.__floor__()
    
    def __trunc__(self):
        return self.puntos.__trunc__()
    
    def __round__(self, n=0):
        return self.puntos.__round__(n)
    
    
    def __getitem__(self, key):
        return self.puntos.__getitem__(key)

    def __setitem__(self, key, value):
        self.puntos.__setitem__(key, value)
        return self.puntos
    
    def __delitem__(self, key):
        self.puntos.__delitem__(key)
        return self.puntos
    
    def __contains__(self, item):
        return self.puntos.__contains__(item)
    
    def __len__(self):
        return self.puntos.__len__()
    
    def __iter__(self):
        return self.puntos.__iter__()
    
    def __reversed__(self):
        return self.puntos.__reversed__()
    
    def __repr__(self):
        return self.puntos.__repr__()
    
    def __str__(self):
        return self.puntos.__str__()
    
    def __format__(self, format_spec):
        return self.puntos.__format__(format_spec)
    
    def __hash__(self):
        return self.puntos.__hash__()
    
    def __bool__(self):
        return self.puntos.__bool__()
    
    def __index__(self):
        return self.puntos.__index__()
    
    def __coerce__(self, other):
        return self.puntos.__coerce__(other)
    
    def __enter__(self):
        return self.puntos.__enter__()
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.puntos.__exit__(exc_type, exc_value, traceback)
    
    def __trunc__(self):
        return self.puntos.__trunc__()
    
    def __round__(self, n=0):
        return self.puntos.__round__(n)
    
    def __ceil__(self):
        return self.puntos.__ceil__()
    
    def __floor__(self):
        return self.puntos.__floor__()
    

    def __getattr__(self, name):
        return getattr(self.puntos, name)
    
    def __setattr__(self, name, value):
        setattr(self.puntos, name, value)
        return self.puntos
    
    def __delattr__(self, name):
        delattr(self.puntos, name)
        return self.puntos
    
    def __dir__(self):
        return dir(self.puntos)
    
    def __instancecheck__(self, instance):
        return self.puntos.__instancecheck__(instance)
    
    def __subclasscheck__(self, subclass):
        return self.puntos.__subclasscheck__(subclass)
    
    def __call__(self, *args, **kwargs):
        return self.puntos.__call__(*args, **kwargs)
    
    def __getattribute__(self, name):
        return getattribute(self.puntos, name)
    
    def __setattribute__(self, name, value):
        setattribute(self.puntos, name, value)
        return self.puntos
    
    def __delattribute__(self, name):
        delattribute(self.puntos, name)
        return self.puntos
    
getattribute = __getattr__ = __getattribute__ = getattr
setattribute = __setattr__ = __setattribute__ = setattr
delattribute =  __delattr__ = __delattribute__ = delattr
dir = __dir__ = __dir__ = dir
instancecheck = __instancecheck__ = __instancecheck__ = isinstance
subclasscheck = __subclasscheck__ = __subclasscheck__ = issubclass
call = __call__ = __call__  = Call

class Mesa:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.jugadores = []
        self.puntos = 0
        self.puntos_jugadores = []
        self.puntos_jugadores_ordenados = []
        self.puntos_jugadores_ordenados_por_nombre = []
        self.puntos_jugadores_ordenados_por_numero = []
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        self.puntos_jugadores.append(jugador.puntos)
        self.puntos_jugadores_ordenados = sorted(self.puntos_jugadores, reverse=True)
        self.puntos_jugadores_ordenados_por_nombre = sorted(self.puntos_jugadores_ordenados, key=lambda x: x.nombre, reverse=True)
        self.puntos_jugadores_ordenados_por_numero = sorted(self.puntos_jugadores_ordenados, key=lambda x: x.numero, reverse=True)
        
    def __str__(self):
        return f"{self.nombre} {self.numero}"

    def __repr__(self):
        return f"{self.nombre} {self.numero}"
    
    def __getitem__(self, key):
        return self.jugadores.__getitem__(key)

    def __setitem__(self, key, value):
        self.jugadores.__setitem__(key, value)
        return self.jugadores
    
    def __delitem__(self, key):
        self.jugadores.__delitem__(key)
        return self.jugadores
    
    def __contains__(self, item):
        return self.jugadores.__contains__(item)
    
    def __len__(self):
        return self.jugadores.__len__()
    
    def __iter__(self):
        return self.jugadores.__iter__()
    
    def __reversed__(self):
        return self.jugadores.__reversed__()
    
    def __repr__(self):
        return self.jugadores.__repr__()
    
    def __str__(self):
        return self.jugadores.__str__()
    
    def __format__(self, format_spec):
        return self.jugadores.__format__(format_spec)
    
    def __hash__(self):
        return self.jugadores.__hash__()
    
    def __bool__(self):
        return self.jugadores.__bool__()
    
    def __index__(self):
        return self.jugadores.__index__()
    
    def __coerce__(self, other):
        return self.jugadores.__coerce__(other)
    
    def __enter__(self):
        return self.jugadores.__enter__()
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.jugadores.__exit__(exc_type, exc_value, traceback)
    
    def __trunc__(self):
        return self.jugadores.__trunc__()
    
    def __round__(self, n=0):
        return self.jugadores.__round__(n)
    
    def __ceil__(self):
        return self.jugadores.__ceil__()
    
    def __floor__(self):
        return self.jugadores.__floor__()
    
    
    def __getattr__(self, name):
        return getattr(self.jugadores, name)

    def __setattr__(self, name, value):
        setattr(self.jugadores, name, value)
        return self.jugadores
    
    def __delattr__(self, name):
        delattr(self.jugadores, name)
        return self.jugadores
    
    def __dir__(self):
        return dir(self.jugadores)
    
    def __instancecheck__(self, instance):
        return self.jugadores.__instancecheck__(instance)
    
    def __subclasscheck__(self, subclass):
        return self.jugadores.__subclasscheck__(subclass)
    
    def __call__(self, *args, **kwargs):
        return self.jugadores.__call__(*args, **kwargs)
    
    def __getattribute__(self, name):
        return getattribute(self.jugadores, name)
    
    def __setattribute__(self, name, value):
        setattribute(self.jugadores, name, value)
        return self.jugadores
    
    def __delattribute__(self, name):
        delattribute(self.jugadores, name)
        return self.jugadores
    
getattribute = __getattr__ = __getattribute__ = getattr
setattribute = __setattr__ = __setattribute__ = setattr
delattribute =  __delattr__ = __delattribute__ = delattr
dir = __dir__ = __dir__ = dir
instancecheck = __instancecheck__ = __instancecheck__ = isinstance
subclasscheck = __subclasscheck__ = __subclasscheck__ = issubclass
call = __call__ = __call__  = Call


#importamos una libreria de python para trabajar con graficos
import matplotlib.pyplot as plt

#creamos la interfaz grafica para el usuario
class InterfazGrafica:
    def __init__(self, mesas):
        self.mesas = mesas
        self.mesas_ordenadas = sorted(self.mesas, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_nombre = sorted(self.mesas_ordenadas, key=lambda x: x.nombre, reverse=True)
        self.mesas_ordenadas_por_numero = sorted(self.mesas_ordenadas, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_puntos = sorted(self.mesas_ordenadas, key=lambda x: x.puntos, reverse=True)
        self.mesas_ordenadas_por_puntos_por_nombre = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.nombre, reverse=True)
        self.mesas_ordenadas_por_puntos_por_numero = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_puntos_por_puntos = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.puntos, reverse=True)
        self.jugadores = []
        self.jugadores_ordenados = []
        self.jugadores_ordenados_por_nombre = []
        self.jugadores_ordenados_por_numero = []
        self.jugadores_ordenados_por_puntos = []
        
#damos un nombre a la ventana
        Tkinter = Tkinter.Tk()
        Tk = Tkinter.Tk()
        self.ventana = Tk()
        self.ventana.title("Mesas")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

#creamos una funcion para cerrar la ventana
    def cerrar_ventana(self):
        self.ventana.destroy()
        self.ventana.quit()
        exit()
        
#creamos una funcion para crear una mesa
    def crear_mesa(self):
        self.mesa = Mesa()
        self.mesas.append(self.mesa)
        self.mesas_ordenadas = sorted(self.mesas, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_nombre = sorted(self.mesas_ordenadas, key=lambda x: x.nombre, reverse=True)
        self.mesas_ordenadas_por_numero = sorted(self.mesas_ordenadas, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_puntos = sorted(self.mesas_ordenadas, key=lambda x: x.puntos, reverse=True)
        self.mesas_ordenadas_por_puntos_por_nombre = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.nombre, reverse=True)
        self.mesas_ordenadas_por_puntos_por_numero = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.numero, reverse=True)
        self.mesas_ordenadas_por_puntos_por_puntos = sorted(self.mesas_ordenadas_por_puntos, key=lambda x: x.puntos, reverse=True)
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Mesas")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#creamos una funcion para crear un jugador
    def crear_jugador(self):
        Jugador = self.ventana.Jugador.get()
        self.jugador = Jugador()
        self.jugadores.append(self.jugador)
        self.jugadores_ordenados = sorted(self.jugadores, key=lambda x: x.nombre, reverse=True)
        self.jugadores_ordenados_por_nombre = sorted(self.jugadores_ordenados, key=lambda x: x.nombre, reverse=True)
        self.jugadores_ordenados_por_numero = sorted(self.jugadores_ordenados, key=lambda x: x.numero, reverse=True)
        self.jugadores_ordenados_por_puntos = sorted(self.jugadores_ordenados, key=lambda x: x.puntos, reverse=True)
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Jugadores")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#creamos una funcion para crear una partida
    def crear_partida(self):
        Partida = self.ventana.Partida.get()
        self.partida = Partida()
        self.partidas.append(self.partida)
        self.partidas_ordenadas = sorted(self.partidas, key=lambda x: x.numero, reverse=True)
        self.partidas_ordenadas_por_nombre = sorted(self.partidas_ordenadas, key=lambda x: x.nombre, reverse=True)
        self.partidas_ordenadas_por_numero = sorted(self.partidas_ordenadas, key=lambda x: x.numero, reverse=True)
        self.partidas_ordenadas_por_puntos = sorted(self.partidas_ordenadas, key=lambda x: x.puntos, reverse=True)
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Partidas")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#creamos una funcion para crear una ronda
    def crear_ronda(self):
        Ronda = self.ventana.Ronda.get()
        self.ronda = Ronda()
        self.rondas.append(self.ronda)
        self.rondas_ordenadas = sorted(self.rondas, key=lambda x: x.numero, reverse=True)
        self.rondas_ordenadas_por_nombre = sorted(self.rondas_ordenadas, key=lambda x: x.nombre, reverse=True)
        self.rondas_ordenadas_por_numero = sorted(self.rondas_ordenadas, key=lambda x: x.numero, reverse=True)
        self.rondas_ordenadas_por_puntos = sorted(self.rondas_ordenadas, key=lambda x: x.puntos, reverse=True)
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Rondas")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#creamos una funcion para el juego
    def juego(self):
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Juego")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#incluimos todas las condiciones de juego
    def juego_condiciones(self):
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Juego")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#incluimos todas las cartas de juego
    def juego_cartas(self):
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Juego")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()
        
#incluimos un menu para elegir el juego
    def juego_menu(self):
        self.ventana.destroy()
        self.ventana.quit()
        Tkinter = Tkinter.Tk()
        self.ventana = Tkinter.Tk()
        self.ventana.title("Juego")
        self.ventana.geometry("800x600")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="white")
        self.ventana.iconbitmap("icono.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana.mainloop()



        

        

        

    
        
        
    