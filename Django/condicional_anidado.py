# condicional anidado

"""
edad = int(input("Cuántos años tienes?: "))

graduacion = input("Ya te has graduado?(si) o (no): ")

if edad > 18:
    print("Felicidades, ya eres mayor de edad")
    if graduacion == "si":
        print("Felicidades por estar ya graduado!")
"""

password = input("Por favor, ingrese la contraseña: ")

if len(password) >= 8:
    print("Correcto, contraseña cumple parámetros establecidos")

    if password == "watermelon":
        print("Contraseña correcta, bienvenido al sistema")
    else:
        print("Contraseña Incorrecta")
else:
    print("Tu contraseña es correcta pero insegura")
    print("Contraseña Incorrecta")









