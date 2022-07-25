# f-strings

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apelllido = apellido
        self.edad = edad

    # def __str__(self):
    def __repr__(self):
        return f"Hola, que tal? Me llamo {self.nombre} {self.apelllido} y tengo {self.edad} años"


nuevo_estudiante = Estudiante("Erick", "Zanussem", 46)
# print(f"{nuevo_estudiante}")
print(f"{nuevo_estudiante !r} ")



