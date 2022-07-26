
# Realizar un programa que conste de una clase Persona con dos atributos nombre y edad. Los atributos se introducirán por teclado y habrá otro método para imprimir los datos.

# Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo. Debe mostrar si tiene que pagar impuestos o no (sueldo superior a 3000).

# Crear un objeto de cada clase.

# Especificaciones:
# declarar clases y atributos
# debe crear un objeto de cada clase
# imprimir si el empleado debe pagar impuestos o no

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def imprimir(self):
        super().imprimir()
        print("Sueldo: ", self.sueldo)
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")

Empleado1 = Empleado("Juan", 30, 2000)
Empleado1.imprimir()









