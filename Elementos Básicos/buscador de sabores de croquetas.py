#inicia el programa del buscador de sabores de croquetas con un saludo
print("Bienvenido al buscador de sabores de croquetas")
#dice el creador del programa
print("Creado por:")
print("Erick Zanussem")
#pide el nombre de croqueta
print("Ingrese el nombre de la croqueta:")
#crea una variable para la croqueta
croqueta = input()
#crea una variable para la croqueta
print("Ingrese el nombre de la croqueta:")
#lista de sabores de croquetas

sabor_1 = "croquetas de jamón"
sabor_2 = "croquetas de queso"
sabor_3 = "croquetas de queso y jamón"
sabor_4 = "croquetas de queso y jamón y tocino"
sabor_5 = "croquetas de queso y jamón y tocino y salchicha"
sabor_6 = "croquetas morcilla"
sabor_7 = "croquetas de cocido"
sabor_8 = "croquetas de tocino"
sabor_9 = "croquetas de salchicha"
sabor_10 = "croquetas de salchicha y tocino"
sabor_11 = "croquetas de salchicha y tocino y jamón"
sabor_12 = "croquetas de salchicha y tocino y jamón y queso"
sabor_13 = "croquetas de salchicha y tocino y jamón y queso y tocino"
sabor_14 = "croquetas de pescado"
sabor_15 = "croquetas de pescado y tocino"
sabor_16 = "croquetas de pescado y tocino y jamón"
sabor_17 = "croquetas de pescado y tocino y jamón y queso"
sabor_18 = "croquetas de pescado y tocino y jamón y queso y tocino"
sabor_19 = "croquetas de restos del día anterior"
    
#si un sabor es encontrado, se muestra el sabor
if croqueta == sabor_1:
    print("Sabor encontrado:", sabor_1)
elif croqueta == sabor_2:
    print("Sabor encontrado:", sabor_2)
elif croqueta == sabor_3:
    print("Sabor encontrado:", sabor_3)
elif croqueta == sabor_4:
    print("Sabor encontrado:", sabor_4)
elif croqueta == sabor_5:
    print("Sabor encontrado:", sabor_5)
elif croqueta == sabor_6:
    print("Sabor encontrado:", sabor_6)
elif croqueta == sabor_7:
    print("Sabor encontrado:", sabor_7)
elif croqueta == sabor_8:
    print("Sabor encontrado:", sabor_8)
elif croqueta == sabor_9:
    print("Sabor encontrado:", sabor_9)
elif croqueta == sabor_10:
    print("Sabor encontrado:", sabor_10)
elif croqueta == sabor_11:
    print("Sabor encontrado:", sabor_11)
elif croqueta == sabor_12:
    print("Sabor encontrado:", sabor_12)
elif croqueta == sabor_13:
    print("Sabor encontrado:", sabor_13)
elif croqueta == sabor_14:
    print("Sabor encontrado:", sabor_14)
elif croqueta == sabor_15:
    print("Sabor encontrado:", sabor_15)
elif croqueta == sabor_16:
    print("Sabor encontrado:", sabor_16)
elif croqueta == sabor_17:
    print("Sabor encontrado:", sabor_17)
elif croqueta == sabor_18:
    print("Sabor encontrado:", sabor_18)
elif croqueta == sabor_19:
    print("Sabor encontrado:", sabor_19)
else:
    print("No se encontró el sabor")

#genera una lista con los sabores de croquetas
lista_sabores = [sabor_1, sabor_2, sabor_3, sabor_4, sabor_5, sabor_6, sabor_7, sabor_8, sabor_9, sabor_10, sabor_11, sabor_12, sabor_13, sabor_14, sabor_15, sabor_16, sabor_17, sabor_18, sabor_19]
#muestra la lista de sabores
print("Lista de sabores:", lista_sabores)
#pide eleccion de sabores
print("Ingrese el número de sabores que desea:")
#crea una variable para la eleccion de sabores
eleccion = int(input())
#crea una variable para saber si el sabor esta en la lista
encontrado = False
#crea una variable para saber si el sabor esta en la lista
for sabor in lista_sabores:
    if sabor == croqueta:
        encontrado = True
#si el sabor esta en la lista, se muestra el sabor
if encontrado == True:
    print("Sabor encontrado:", croqueta)
#si el sabor no esta en la lista, se muestra el sabor
else:
    print("No se encontró el sabor")
#crea una lista para los sabores elegidos
sabores_elegidos = []
#crea una lista para los sabores no elegidos
sabores_no_elegidos = []
#muestra la lista de sabores elegidos
print("Sabores elegidos:")
#muestra la lista de sabores no elegidos
print("Sabores no elegidos:")
#crea una variable para el contador de sabores elegidos
contador_sabores_elegidos = 0
#crea una variable para el contador de sabores no elegidos
contador_sabores_no_elegidos = 0
#crea una variable para el contador de sabores
contador_sabores = 0
#da gracias a Nuria por su labor de ayudarme
print("Gracias a Nuria por su labor de ayudarme y su larga experiencia con las croquetas")
#fin del programa
print("Fin del programa")
#despedida
print("Gracias por usar el buscador de sabores de croquetas")
print("Adios")

    
