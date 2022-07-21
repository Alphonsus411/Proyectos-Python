# Escribir un programa que almacene en una variable cualquier contraseña (invéntela), por ejemplo, condicional,
# luego pida al usuario que ingrese una contraseña e imprima por pantalla si la introducida por el usuario coincide
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. Nota: Considere se debe únicamente
# mostrar los mensajes de confirmación al finalizar el programa, el usuario puede introducir la contraseña 3 veces
# antes de mostrar el resultado, al menos que la ingrese correctamente.

def contraseña_acceso():
    contraseña: str =  input("Por favor, introduzca su contraseña: ")
    if contraseña == "covabunga":
        print("acceso permitido")
    else:
        print("acceso denegado, por favor repita la contraseña")






