# Escribir un programa que almacene en una variable cualquier contraseña (invéntela), por ejemplo, condicional,
# luego pida al usuario que ingrese una contraseña e imprima por pantalla si la introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
# Nota: Considere se debe únicamente mostrar los mensajes de confirmación
# al finalizar el programa, el usuario puede introducir la contraseña 3 veces antes de mostrar el resultado, al menos que la ingrese correctamente.

print("Bienvenido a una nueva sesión")
contraseña = "condicional"
contraseña2 = input("Ingrese la contraseña: ")
contraseña3 = input("Ingrese la contraseña: ")
contraseña4 = input("Ingrese la contraseña: ")

# contraseña = "condicional"
if contraseña == contraseña2:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

    if contraseña == contraseña3:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

        if contraseña == contraseña4:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")
            print("Sesión finalizada")

print("Creado por Erick Zanussem")
