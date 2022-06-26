#creamos un inventario de productos
def inventario():
        inventario = {'producto1': {'nombre': 'producto1', 'precio': '$10', 'cantidad': '5'},
                      'producto2': {'nombre': 'producto2', 'precio': '$20', 'cantidad': '10'},
                      'producto3': {'nombre': 'producto3', 'precio': '$30', 'cantidad': '15'},
                      'producto4': {'nombre': 'producto4', 'precio': '$40', 'cantidad': '20'},
                      'producto5': {'nombre': 'producto5', 'precio': '$50', 'cantidad': '25'}}
        return inventario
#creamos una funcion para mostrar el inventario
def mostrar_inventario(inventario):
        print('Inventario:')
        for producto in inventario:
            print('{}'.format(producto))
        print('\n')
#creamos una funcion para mostrar el precio de un producto
def mostrar_precio(inventario):
        print('Precio de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['precio']))
        print('\n')
#creamos una funcion para mostrar la cantidad de un producto
def mostrar_cantidad(inventario):
        print('Cantidad de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['cantidad']))
        print('\n')
#creamos una funcion para mostrar el nombre de un producto
def mostrar_nombre(inventario):
        print('Nombre de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['nombre']))
        print('\n')
#creamos una funcion para mostrar el nombre de un producto y su precio
def mostrar_nombre_precio(inventario):
        print('Nombre y precio de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['nombre'] + ' ' + inventario[producto]['precio']))
        print('\n')
#creamos una funcion para mostrar el nombre de un producto y su cantidad
def mostrar_nombre_cantidad(inventario):
        print('Nombre y cantidad de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['nombre'] + ' ' + inventario[producto]['cantidad']))
        print('\n')
#creamos una funcion para mostrar el nombre de un producto y su precio y cantidad
def mostrar_nombre_precio_cantidad(inventario):
        print('Nombre, precio y cantidad de los productos:')
        for producto in inventario:
            print('{}'.format(inventario[producto]['nombre'] + ' ' + inventario[producto]['precio'] + ' ' + inventario[producto]['cantidad']))
        print('\n')
#generamos un informe de inventario
def informe(inventario):
        print('Informe de inventario:')
        print('\n')
        mostrar_inventario(inventario)
        mostrar_precio(inventario)
        mostrar_cantidad(inventario)
        mostrar_nombre(inventario)
        mostrar_nombre_precio(inventario)
        mostrar_nombre_cantidad(inventario)
        mostrar_nombre_precio_cantidad(inventario)

#ejecutamos la funcion
informe(inventario())

#separamos los productos por tipo
def separar_productos(inventario):
    productos_tipo1 = []
    productos_tipo2 = []
    productos_tipo3 = []
    productos_tipo4 = []
    productos_tipo5 = []
    for producto in inventario:
        if inventario[producto]['nombre'] == 'producto1':
            productos_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2':
            productos_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3':
            productos_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4':
            productos_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5':
            productos_tipo5.append(inventario[producto]['nombre'])
    return productos_tipo1, productos_tipo2, productos_tipo3, productos_tipo4, productos_tipo5

#separamos los productos por seccion
def separar_productos_seccion(inventario):
    productos_seccion1 = []
    productos_seccion2 = []
    productos_seccion3 = []
    productos_seccion4 = []
    productos_seccion5 = []
    for producto in inventario:
        if inventario[producto]['nombre'] == 'producto1':
            productos_seccion1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2':
            productos_seccion2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3':
            productos_seccion3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4':
            productos_seccion4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5':
            productos_seccion5.append(inventario[producto]['nombre'])
    return productos_seccion1, productos_seccion2, productos_seccion3, productos_seccion4, productos_seccion5

#separamos los productos por seccion y tipo
def separar_productos_seccion_tipo(inventario):
    productos_seccion1_tipo1 = []
    productos_seccion1_tipo2 = []
    productos_seccion1_tipo3 = []
    productos_seccion1_tipo4 = []
    productos_seccion1_tipo5 = []
    productos_seccion2_tipo1 = []
    productos_seccion2_tipo2 = []
    productos_seccion2_tipo3 = []
    productos_seccion2_tipo4 = []
    productos_seccion2_tipo5 = []
    productos_seccion3_tipo1 = []
    productos_seccion3_tipo2 = []
    productos_seccion3_tipo3 = []
    productos_seccion3_tipo4 = []
    productos_seccion3_tipo5 = []
    productos_seccion4_tipo1 = []
    productos_seccion4_tipo2 = []
    productos_seccion4_tipo3 = []
    productos_seccion4_tipo4 = []
    productos_seccion4_tipo5 = []
    productos_seccion5_tipo1 = []
    productos_seccion5_tipo2 = []
    productos_seccion5_tipo3 = []
    productos_seccion5_tipo4 = []
    productos_seccion5_tipo5 = []
    for producto in inventario:
        if inventario[producto]['nombre'] == 'producto1' and inventario[producto]['seccion'] == 'seccion1':
            productos_seccion1_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2' and inventario[producto]['seccion'] == 'seccion1':
            productos_seccion1_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3' and inventario[producto]['seccion'] == 'seccion1':
            productos_seccion1_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4' and inventario[producto]['seccion'] == 'seccion1':
            productos_seccion1_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5' and inventario[producto]['seccion'] == 'seccion1':
            productos_seccion1_tipo5.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto1' and inventario[producto]['seccion'] == 'seccion2':
            productos_seccion2_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2' and inventario[producto]['seccion'] == 'seccion2':
            productos_seccion2_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3' and inventario[producto]['seccion'] == 'seccion2':
            productos_seccion2_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4' and inventario[producto]['seccion'] == 'seccion2':
            productos_seccion2_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5' and inventario[producto]['seccion'] == 'seccion2':
            productos_seccion2_tipo5.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto1' and inventario[producto]['seccion'] == 'seccion3':
            productos_seccion3_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2' and inventario[producto]['seccion'] == 'seccion3':
            productos_seccion3_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3' and inventario[producto]['seccion'] == 'seccion3':
            productos_seccion3_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4' and inventario[producto]['seccion'] == 'seccion3':
            productos_seccion3_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5' and inventario[producto]['seccion'] == 'seccion3':
            productos_seccion3_tipo5.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto1' and inventario[producto]['seccion'] == 'seccion4':
            productos_seccion4_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2' and inventario[producto]['seccion'] == 'seccion4':
            productos_seccion4_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3' and inventario[producto]['seccion'] == 'seccion4':
            productos_seccion4_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4' and inventario[producto]['seccion'] == 'seccion4':
            productos_seccion4_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5' and inventario[producto]['seccion'] == 'seccion4':
            productos_seccion4_tipo5.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto1' and inventario[producto]['seccion'] == 'seccion5':
            productos_seccion5_tipo1.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto2' and inventario[producto]['seccion'] == 'seccion5':
            productos_seccion5_tipo2.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto3' and inventario[producto]['seccion'] == 'seccion5':
            productos_seccion5_tipo3.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto4' and inventario[producto]['seccion'] == 'seccion5':
            productos_seccion5_tipo4.append(inventario[producto]['nombre'])
        elif inventario[producto]['nombre'] == 'producto5' and inventario[producto]['seccion'] == 'seccion5':
            productos_seccion5_tipo5.append(inventario[producto]['nombre'])

#definimos los productos de cada seccion
productos_seccion1 = {'tipo1': productos_seccion1_tipo1, 'tipo2': productos_seccion1_tipo2, 'tipo3': productos_seccion1_tipo3, 'tipo4': productos_seccion1_tipo4, 'tipo5': productos_seccion1_tipo5}
productos_seccion2 = {'tipo1': productos_seccion2_tipo1, 'tipo2': productos_seccion2_tipo2, 'tipo3': productos_seccion2_tipo3, 'tipo4': productos_seccion2_tipo4, 'tipo5': productos_seccion2_tipo5}
productos_seccion3 = {'tipo1': productos_seccion3_tipo1, 'tipo2': productos_seccion3_tipo2, 'tipo3': productos_seccion3_tipo3, 'tipo4': productos_seccion3_tipo4, 'tipo5': productos_seccion3_tipo5}
productos_seccion4 = {'tipo1': productos_seccion4_tipo1, 'tipo2': productos_seccion4_tipo2, 'tipo3': productos_seccion4_tipo3, 'tipo4': productos_seccion4_tipo4, 'tipo5': productos_seccion4_tipo5}
productos_seccion5 = {'tipo1': productos_seccion5_tipo1, 'tipo2': productos_seccion5_tipo2, 'tipo3': productos_seccion5_tipo3, 'tipo4': productos_seccion5_tipo4, 'tipo5': productos_seccion5_tipo5}
        
#definimos los productos de cada seccion por tipo
productos_seccion1_tipo1 = {'producto1': productos_seccion1_tipo1[0], 'producto2': productos_seccion1_tipo1[1], 'producto3': productos_seccion1_tipo1[2], 'producto4': productos_seccion1_tipo1[3], 'producto5': productos_seccion1_tipo1[4]}
productos_seccion1_tipo2 = {'producto1': productos_seccion1_tipo2[0], 'producto2': productos_seccion1_tipo2[1], 'producto3': productos_seccion1_tipo2[2], 'producto4': productos_seccion1_tipo2[3], 'producto5': productos_seccion1_tipo2[4]}
productos_seccion1_tipo3 = {'producto1': productos_seccion1_tipo3[0], 'producto2': productos_seccion1_tipo3[1], 'producto3': productos_seccion1_tipo3[2], 'producto4': productos_seccion1_tipo3[3], 'producto5': productos_seccion1_tipo3[4]}
productos_seccion1_tipo4 = {'producto1': productos_seccion1_tipo4[0], 'producto2': productos_seccion1_tipo4[1], 'producto3': productos_seccion1_tipo4[2], 'producto4': productos_seccion1_tipo4[3], 'producto5': productos_seccion1_tipo4[4]}
productos_seccion1_tipo5 = {'producto1': productos_seccion1_tipo5[0], 'producto2': productos_seccion1_tipo5[1], 'producto3': productos_seccion1_tipo5[2], 'producto4': productos_seccion1_tipo5[3], 'producto5': productos_seccion1_tipo5[4]}
productos_seccion2_tipo1 = {'producto1': productos_seccion2_tipo1[0], 'producto2': productos_seccion2_tipo1[1], 'producto3': productos_seccion2_tipo1[2], 'producto4': productos_seccion2_tipo1[3], 'producto5': productos_seccion2_tipo1[4]}
productos_seccion2_tipo2 = {'producto1': productos_seccion2_tipo2[0], 'producto2': productos_seccion2_tipo2[1], 'producto3': productos_seccion2_tipo2[2], 'producto4': productos_seccion2_tipo2[3], 'producto5': productos_seccion2_tipo2[4]}
productos_seccion2_tipo3 = {'producto1': productos_seccion2_tipo3[0], 'producto2': productos_seccion2_tipo3[1], 'producto3': productos_seccion2_tipo3[2], 'producto4': productos_seccion2_tipo3[3], 'producto5': productos_seccion2_tipo3[4]}
productos_seccion2_tipo4 = {'producto1': productos_seccion2_tipo4[0], 'producto2': productos_seccion2_tipo4[1], 'producto3': productos_seccion2_tipo4[2], 'producto4': productos_seccion2_tipo4[3], 'producto5': productos_seccion2_tipo4[4]}
productos_seccion2_tipo5 = {'producto1': productos_seccion2_tipo5[0], 'producto2': productos_seccion2_tipo5[1], 'producto3': productos_seccion2_tipo5[2], 'producto4': productos_seccion2_tipo5[3], 'producto5': productos_seccion2_tipo5[4]}
productos_seccion3_tipo1 = {'producto1': productos_seccion3_tipo1[0], 'producto2': productos_seccion3_tipo1[1], 'producto3': productos_seccion3_tipo1[2], 'producto4': productos_seccion3_tipo1[3], 'producto5': productos_seccion3_tipo1[4]}
productos_seccion3_tipo2 = {'producto1': productos_seccion3_tipo2[0], 'producto2': productos_seccion3_tipo2[1], 'producto3': productos_seccion3_tipo2[2], 'producto4': productos_seccion3_tipo2[3], 'producto5': productos_seccion3_tipo2[4]}
productos_seccion3_tipo3 = {'producto1': productos_seccion3_tipo3[0], 'producto2': productos_seccion3_tipo3[1], 'producto3': productos_seccion3_tipo3[2], 'producto4': productos_seccion3_tipo3[3], 'producto5': productos_seccion3_tipo3[4]}
productos_seccion3_tipo4 = {'producto1': productos_seccion3_tipo4[0], 'producto2': productos_seccion3_tipo4[1], 'producto3': productos_seccion3_tipo4[2], 'producto4': productos_seccion3_tipo4[3], 'producto5': productos_seccion3_tipo4[4]}
productos_seccion3_tipo5 = {'producto1': productos_seccion3_tipo5[0], 'producto2': productos_seccion3_tipo5[1], 'producto3': productos_seccion3_tipo5[2], 'producto4': productos_seccion3_tipo5[3], 'producto5': productos_seccion3_tipo5[4]}
productos_seccion4_tipo1 = {'producto1': productos_seccion4_tipo1[0], 'producto2': productos_seccion4_tipo1[1], 'producto3': productos_seccion4_tipo1[2], 'producto4': productos_seccion4_tipo1[3], 'producto5': productos_seccion4_tipo1[4]}
productos_seccion4_tipo2 = {'producto1': productos_seccion4_tipo2[0], 'producto2': productos_seccion4_tipo2[1], 'producto3': productos_seccion4_tipo2[2], 'producto4': productos_seccion4_tipo2[3], 'producto5': productos_seccion4_tipo2[4]}
productos_seccion4_tipo3 = {'producto1': productos_seccion4_tipo3[0], 'producto2': productos_seccion4_tipo3[1], 'producto3': productos_seccion4_tipo3[2], 'producto4': productos_seccion4_tipo3[3], 'producto5': productos_seccion4_tipo3[4]}
productos_seccion4_tipo4 = {'producto1': productos_seccion4_tipo4[0], 'producto2': productos_seccion4_tipo4[1], 'producto3': productos_seccion4_tipo4[2], 'producto4': productos_seccion4_tipo4[3], 'producto5': productos_seccion4_tipo4[4]}
productos_seccion4_tipo5 = {'producto1': productos_seccion4_tipo5[0], 'producto2': productos_seccion4_tipo5[1], 'producto3': productos_seccion4_tipo5[2], 'producto4': productos_seccion4_tipo5[3], 'producto5': productos_seccion4_tipo5[4]}
productos_seccion5_tipo1 = {'producto1': productos_seccion5_tipo1[0], 'producto2': productos_seccion5_tipo1[1], 'producto3': productos_seccion5_tipo1[2], 'producto4': productos_seccion5_tipo1[3], 'producto5': productos_seccion5_tipo1[4]}
productos_seccion5_tipo2 = {'producto1': productos_seccion5_tipo2[0], 'producto2': productos_seccion5_tipo2[1], 'producto3': productos_seccion5_tipo2[2], 'producto4': productos_seccion5_tipo2[3], 'producto5': productos_seccion5_tipo2[4]}
productos_seccion5_tipo3 = {'producto1': productos_seccion5_tipo3[0], 'producto2': productos_seccion5_tipo3[1], 'producto3': productos_seccion5_tipo3[2], 'producto4': productos_seccion5_tipo3[3], 'producto5': productos_seccion5_tipo3[4]}
productos_seccion5_tipo4 = {'producto1': productos_seccion5_tipo4[0], 'producto2': productos_seccion5_tipo4[1], 'producto3': productos_seccion5_tipo4[2], 'producto4': productos_seccion5_tipo4[3], 'producto5': productos_seccion5_tipo4[4]}
productos_seccion5_tipo5 = {'producto1': productos_seccion5_tipo5[0], 'producto2': productos_seccion5_tipo5[1], 'producto3': productos_seccion5_tipo5[2], 'producto4': productos_seccion5_tipo5[3], 'producto5': productos_seccion5_tipo5[4]}

# Se imprime el inventario
print('Inventario:')
print('Seccion 1:')
print('Tipo 1:', productos_seccion1_tipo1)
print('Tipo 2:', productos_seccion1_tipo2)
print('Tipo 3:', productos_seccion1_tipo3)
print('Tipo 4:', productos_seccion1_tipo4)
print('Tipo 5:', productos_seccion1_tipo5)
print('Seccion 2:')
print('Tipo 1:', productos_seccion2_tipo1)
print('Tipo 2:', productos_seccion2_tipo2)
print('Tipo 3:', productos_seccion2_tipo3)
print('Tipo 4:', productos_seccion2_tipo4)
print('Tipo 5:', productos_seccion2_tipo5)
print('Seccion 3:')
print('Tipo 1:', productos_seccion3_tipo1)
print('Tipo 2:', productos_seccion3_tipo2)
print('Tipo 3:', productos_seccion3_tipo3)
print('Tipo 4:', productos_seccion3_tipo4)
print('Tipo 5:', productos_seccion3_tipo5)
print('Seccion 4:')
print('Tipo 1:', productos_seccion4_tipo1)
print('Tipo 2:', productos_seccion4_tipo2)
print('Tipo 3:', productos_seccion4_tipo3)
print('Tipo 4:', productos_seccion4_tipo4)
print('Tipo 5:', productos_seccion4_tipo5)
print('Seccion 5:')
print('Tipo 1:', productos_seccion5_tipo1)
print('Tipo 2:', productos_seccion5_tipo2)
print('Tipo 3:', productos_seccion5_tipo3)
print('Tipo 4:', productos_seccion5_tipo4)
print('Tipo 5:', productos_seccion5_tipo5)
print('\n')

# Se imprime el inventario ordenado por seccion
print('Inventario ordenado por seccion:')
print('Seccion 1:')
print('Tipo 1:', productos_seccion1_tipo1)
print('Tipo 2:', productos_seccion1_tipo2)
print('Tipo 3:', productos_seccion1_tipo3)
print('Tipo 4:', productos_seccion1_tipo4)
print('Tipo 5:', productos_seccion1_tipo5)
print('Seccion 2:')
print('Tipo 1:', productos_seccion2_tipo1)
print('Tipo 2:', productos_seccion2_tipo2)
print('Tipo 3:', productos_seccion2_tipo3)
print('Tipo 4:', productos_seccion2_tipo4)
print('Tipo 5:', productos_seccion2_tipo5)
print('Seccion 3:')
print('Tipo 1:', productos_seccion3_tipo1)
print('Tipo 2:', productos_seccion3_tipo2)
print('Tipo 3:', productos_seccion3_tipo3)
print('Tipo 4:', productos_seccion3_tipo4)
print('Tipo 5:', productos_seccion3_tipo5)
print('Seccion 4:')
print('Tipo 1:', productos_seccion4_tipo1)
print('Tipo 2:', productos_seccion4_tipo2)
print('Tipo 3:', productos_seccion4_tipo3)
print('Tipo 4:', productos_seccion4_tipo4)
print('Tipo 5:', productos_seccion4_tipo5)
print('Seccion 5:')
print('Tipo 1:', productos_seccion5_tipo1)
print('Tipo 2:', productos_seccion5_tipo2)
print('Tipo 3:', productos_seccion5_tipo3)
print('Tipo 4:', productos_seccion5_tipo4)
print('Tipo 5:', productos_seccion5_tipo5)
print('\n')

# Se imprime el inventario ordenado por nombre
print('Inventario ordenado por nombre:')
print('Seccion 1:')
print('Tipo 1:', productos_seccion1_tipo1)
print('Tipo 2:', productos_seccion1_tipo2)
print('Tipo 3:', productos_seccion1_tipo3)
print('Tipo 4:', productos_seccion1_tipo4)
print('Tipo 5:', productos_seccion1_tipo5)
print('Seccion 2:')
print('Tipo 1:', productos_seccion2_tipo1)
print('Tipo 2:', productos_seccion2_tipo2)
print('Tipo 3:', productos_seccion2_tipo3)
print('Tipo 4:', productos_seccion2_tipo4)
print('Tipo 5:', productos_seccion2_tipo5)
print('Seccion 3:')
print('Tipo 1:', productos_seccion3_tipo1)
print('Tipo 2:', productos_seccion3_tipo2)
print('Tipo 3:', productos_seccion3_tipo3)
print('Tipo 4:', productos_seccion3_tipo4)
print('Tipo 5:', productos_seccion3_tipo5)
print('Seccion 4:')
print('Tipo 1:', productos_seccion4_tipo1)
print('Tipo 2:', productos_seccion4_tipo2)
print('Tipo 3:', productos_seccion4_tipo3)
print('Tipo 4:', productos_seccion4_tipo4)
print('Tipo 5:', productos_seccion4_tipo5)
print('Seccion 5:')
print('Tipo 1:', productos_seccion5_tipo1)
print('Tipo 2:', productos_seccion5_tipo2)
print('Tipo 3:', productos_seccion5_tipo3)
print('Tipo 4:', productos_seccion5_tipo4)
print('Tipo 5:', productos_seccion5_tipo5)
print('\n')

# Se imprime el inventario ordenado por precio
print('Inventario ordenado por precio:')
print('Seccion 1:')
print('Tipo 1:', productos_seccion1_tipo1)
print('Tipo 2:', productos_seccion1_tipo2)
print('Tipo 3:', productos_seccion1_tipo3)
print('Tipo 4:', productos_seccion1_tipo4)
print('Tipo 5:', productos_seccion1_tipo5)
print('Seccion 2:')
print('Tipo 1:', productos_seccion2_tipo1)
print('Tipo 2:', productos_seccion2_tipo2)
print('Tipo 3:', productos_seccion2_tipo3)
print('Tipo 4:', productos_seccion2_tipo4)
print('Tipo 5:', productos_seccion2_tipo5)
print('Seccion 3:')
print('Tipo 1:', productos_seccion3_tipo1)
print('Tipo 2:', productos_seccion3_tipo2)
print('Tipo 3:', productos_seccion3_tipo3)
print('Tipo 4:', productos_seccion3_tipo4)
print('Tipo 5:', productos_seccion3_tipo5)
print('Seccion 4:')
print('Tipo 1:', productos_seccion4_tipo1)
print('Tipo 2:', productos_seccion4_tipo2)
print('Tipo 3:', productos_seccion4_tipo3)
print('Tipo 4:', productos_seccion4_tipo4)
print('Tipo 5:', productos_seccion4_tipo5)
print('Seccion 5:')
print('Tipo 1:', productos_seccion5_tipo1)
print('Tipo 2:', productos_seccion5_tipo2)
print('Tipo 3:', productos_seccion5_tipo3)
print('Tipo 4:', productos_seccion5_tipo4)
print('Tipo 5:', productos_seccion5_tipo5)
print('\n')


            

    