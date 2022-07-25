# Condicionales Anidadas

edad = int(input("Escriba su edad: "))

if 0 >= edad or edad >= 100:
    print('Edad incorrecta')
else:
    print('Edad correcta')
    if edad >= 18:
        print('Es mayor de edad')
