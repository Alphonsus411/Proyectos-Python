"""
Creamos una máquina de caramelos que nos permita comprar caramelos, 
elegir el sabor y el tamaño del caramelo, y que nos devuelva el cambio.

"""

# Creamos una clase llamada MaquinaCaramelos
class MaquinaCaramelos:
    def __init__(self):
        # Inicializamos los atributos de la clase
        self.caramelos = 0
        self.dinero = 0
        self.cambio = 0
        self.sabor = ""
        self.tamaño = ""
        self.precio = 0

    def comprar(self, caramelos):
        # Compramos caramelos
        self.caramelos += caramelos

    def elegir_sabor(self, sabor):
        # Elegimos el sabor del caramelo
        self.sabor = sabor

    def elegir_tamaño(self, tamaño):
        # Elegimos el tamaño del caramelo
        self.tamaño = tamaño

    def insertar_dinero(self, dinero):
        # Insertamos dinero
        self.dinero += dinero

    def devolver_cambio(self):
        # Devolvemos el cambio
        self.cambio = self.dinero - self.precio
        self.dinero = 0
        return self.cambio

    def precio_caramelo(self, precio):
        # Establecemos el precio del caramelo
        self.precio = precio
        
    def __str__(self):
        # Devolvemos una cadena con los datos de la máquina
        return "Caramelos: " + str(self.caramelos) + "  Dinero: " + str(self.dinero) + "  Cambio: " + str(self.cambio) + "  Sabor: " + self.sabor + "  Tamaño: " + self.tamaño + "  Precio: " + str(self.precio)    
    
# Creamos un objeto de la clase MaquinaCaramelos
maquina = MaquinaCaramelos()

# Compramos 10 caramelos
maquina.comprar(10)

# Elegimos el sabor de los caramelos
maquina.elegir_sabor("Fresa")

# Elegimos el tamaño de los caramelos
maquina.elegir_tamaño("Grande")

# Establecemos el precio de los caramelos
maquina.precio_caramelo(0.5)

# Insertamos dinero
maquina.insertar_dinero(1)

# Devolvemos el cambio
cambio = maquina.devolver_cambio()

# Mostramos el cambio
print("Cambio: " + str(cambio))

# Mostramos los datos de la máquina
print(maquina)

# Salida:
# Cambio: 0.5
# Caramelos: 10  Dinero: 0  Cambio: 0  Sabor: Fresa  Tamaño: Grande  Precio: 0.5

    
    