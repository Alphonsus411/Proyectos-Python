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
#crea un pajaro aleatorio 

class pajaro:
    nombre = "jilguero"
    edad = "1"
    color = "black"
    tipo = "semillero"
    
    def __init__(self, nombre, edad, color, tipo):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tipo = tipo
        
print (pajaro.nombre)
print (pajaro.edad)
print (pajaro.color)
print (pajaro.tipo)















    
    


     






        
