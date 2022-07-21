# creamos un diccionario para una lista de frutas y su código correpondiente
frutas = {'mandarina': 84, 'naranja': 96, 'paraguaya': 30552}

# creamos una lista para guardar los códigos de las frutas
codigos = []

# recorremos el diccionario y guardamos los códigos en la lista
for fruta in frutas:
    codigos.append(frutas[fruta])

# ordenamos la lista de códigos
codigos.sort()

# permitimos al usuario introducir una fruta
fruta = input('Introduce una fruta: ')

# comprobamos si la fruta introducida está en el diccionario
if fruta in frutas:
    # si está, mostramos su código
    print('El código de la fruta {} es {}'.format(fruta, frutas[fruta]))

    # buscamos su posición en la lista de códigos
    posicion = codigos.index(frutas[fruta])

    # mostramos la posición de la fruta en la lista de códigos
    print('La fruta {} está en la posición {}'.format(fruta, posicion + 1))
else:
    # si no está, mostramos un mensaje de error
    print('La fruta {} no está en el diccionario'.format(fruta))

# permitimos introducir una nueva fruta y su código, lo incluimos después de la lista de códigos, añadiendo la entrada en el código de la fruta
fruta = input('Introduce una fruta: ')
codigo = int(input('Introduce su código: '))
codigos.append(codigo)
frutas[fruta] = codigo

# ordenamos la lista de códigos de menor a mayor
codigos.sort()

# finalizamos el programa mostrando la lista de códigos ampliada
print('La lista de códigos es: {}'.format(codigos))

# despedimos el programa
print('Gracias por usar el programa')
