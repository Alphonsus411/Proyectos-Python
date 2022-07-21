# funciones para atributos

class Persona:
    edad = 46
    nombre = "Erick"
    pais = "España"


cientifico = Persona()

# print("La edad es: ", cientifico.edad)
# print("La edad es: ", getattr(cientifico, "edad"))
# metodo para obtener la misma funcionalidad anterior, pero con
# una palabra reservada

# print("El cientifico tiene una edad?", hasattr(cientifico, "edad"))
# metodo para comprobar si el atributo existe o no

# setattr(cientifico, 'nombre', 'Aristoteles')
# print(cientifico.nombre)
# metodo para cambiar un atributo

delattr(Persona, "pais")
print(cientifico.edad)
print(cientifico.nombre)


