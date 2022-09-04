# condicional elif

"""
En una escuela de conducción se tiene un programa que,
dependiendo de la edad del usuario,
muestra el tipo de licencia a la que tiene derecho

Condición 1: si es menor de 16, entonces no puede conducir
Condición 2: si es mayor de 18, puede optar a una licencia de conducción
Condición 3: si es menor de 70, puede optar a una licencia estándar
Condición 4: si es mayor de 70, entonces necesita una licencia especial

"""
edad = int(input("Introduzca su edad, por favor: "))

if edad < 16:
    print("No puedes sacarte el carnet de conducir")
elif edad < 18:
    print("Puedes sacarte el carnet de conducir")
elif edad < 70:
    print("Puedes obtener una licencia estándar")
else:
    print("Puedes obtener una licencia especial")
