# herencia

class Vehiculo():  # creamos una clase con sus atributos y unos métodos
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False

    def avanzar(self):  # creamos los métodos asociados a la clase
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f'Matricula: {self.matricula} \n Modelo: {self.modelo} \n Marca: {self.marca} \n Color: {self.color} \n'
              f' Avanzar: {self.avanza} \n Frenar: {self.frena} \n Girar: {self.gira}')
        # Imprimimos los atributos de la clase usando \n para separar los atributos. Hacemos presentes también sus
        # métodos relacionados. Hemos definido la "clase padre".


class Moto(Vehiculo):  # creamos una "clase hija", por ejemplo, el referente a las motocicletas
    def __init__(self, matricula, modelo, marca, color, cilindrada):   # le añadimos una propiedad o atributo
        # específico de las motos
        super().__init__(matricula, modelo, marca, color )  # invocamos con este método los atributos de la clase padre
        self.cilindrada = cilindrada


moto1 = Moto("ABC123", 2018, "BMW", "Rojo", 150)  # creamos un objeto de la "clase hija(Moto)"
moto1.avanzar()
moto1.girar()
moto1.frenar()
print("Cilindrada: " + str(moto1.cilindrada))
moto1.imprimir()



