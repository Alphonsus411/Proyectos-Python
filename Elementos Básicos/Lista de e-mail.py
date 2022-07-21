def correos_completos(clientes):
    resultado = []
    for correo, nombre in clientes:
        resultado.append("{} <{}>".format(nombre, correo))
    return resultado


print(correos_completos([("Adolfo@ejemplo,com", "Adolfo Gonzalez"), ("Isidro@ejemplo.com", "Isidro Gil")]))
