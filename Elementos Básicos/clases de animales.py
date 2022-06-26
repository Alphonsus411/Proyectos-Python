from copyreg import constructor
from email import generator
from itertools import count
from turtle import color

class pajaro (object):
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo
    def __repr__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo
    def __eq__(self, other):
        return self.nombre == other.nombre 
    def __hash__(self):
        return hash(self.nombre)

class reptil (object):
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo
    def __repr__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo
    def __eq__(self, other):
        return self.nombre == other.nombre
    def __hash__(self):
        return hash(self.nombre)

class pez (object):
    def _init_(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
    def __str__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo  
    def __repr__(self):
        return "Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Color: " + self.color + " Tipo: " + self.tipo
    def __eq__(self, other):
        return self.nombre == other.nombre
    def __hash__(self):
        return hash(self.nombre)

#generacion aleatoria de pajaro
def generacion():
    if pajaro is None: return False
    else :
        if pajaro.tipo == "ave":
            return pajaro.tipo
        else:   return False
#generacion aleatoria de reptil
def generacion():
    if reptil is None: return False
    else :
        if reptil.tipo == "ave":
            return reptil.tipo
        else:   return False
#generacion aleatoria de pez
def generacion():
    if pez is None: return False
    else :
        if pez.tipo == "ave":
            return pez.tipo
        else:   return False
        
#crea un pajaro aleatorio y lo agrega a la lista
class pajaro(object):
    nombre = "jilguero"
    edad = "1"
    color = "black"
    tipo = "semillero"
    
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
        
print ("Nombre: " + pajaro.nombre + " Edad: " + str(pajaro.edad) + " Color: " + pajaro.color + " Tipo: " + pajaro.tipo)

#crea un reptil aleatorio y lo agrega a la lista
class reptil(object):
    nombre = "iguana"
    edad = "40"
    color = "verde"
    tipo = "vegetariano"
    
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo

print ("Nombre: " + reptil.nombre + " Edad: " + str(reptil.edad) + " Color: " + reptil.color + " Tipo: " + reptil.tipo)

#crea un pez aleatorio y lo agrega a la lista
class pez(object):
    nombre = "tiburon"
    edad = "10"
    color = "azul"
    tipo = "acuatico"
    
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
        
print ("Nombre: " + pez.nombre + " Edad: " + str(pez.edad) + " Color: " + pez.color + " Tipo: " + pez.tipo)















    
    


     






        
