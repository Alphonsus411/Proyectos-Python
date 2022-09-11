# encapsulamiento

class Persona:
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion  # hacemos el atributo privado mediante dos guiones bajos
        self.nombre = nombre
        self.edad = edad

    def Saludo(self):  # metodo de la clase Persona
        return "Hola" + self.nombre

    def getIdentificacion(self):  # método para acceder al atributo privado
        return self.__identificacion

    def setIdentificacion(self, valor):  # método para cambiar el atributo privado de la identificación
        self.__identificacion = valor


persona1 = Persona(45678, "Erick", 46)  # objeto de la clase Persona

# print(persona1._Persona__identificacion)  # accedemos al atributo privado mediante este tipo de llamada
persona1.setIdentificacion(12345)  # llamada al método de cambio del atributo identificación
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)
