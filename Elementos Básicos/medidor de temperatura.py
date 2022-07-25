# inicia programa


def main():
    print("Bienvenido a la temperatura")
    print("")
    print("1. Mostrar temperatura")
    print("2. Mostrar mapa")
    print("3. Salir")
    print("")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        medicion_temperatura()
    elif opcion == 2:
        datos = tomar_datos()
        mostrar_mapa(datos)
    elif opcion == 3:
        print("Gracias por usar el programa")


# conecta a google
def conectar_google():
    import webbrowser
    import time
    webbrowser.open("https://www.google.com")
    time.sleep(5)
    webbrowser.open("https://www.google.com/maps/@-34.603722,-58.381592,12z")


# crea una clave de acceso
pyowm.OWM('API_KEY')
pyowm = pyowm.OWM('API_KEY')
owm = pyowm.OWM('c9f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8')
# crea una variable para la ciudad
ciudad = input("Ingrese la ciudad: ")
# crea una variable para la temperatura
temperatura = owm.weather_at_place(ciudad)
# crea una variable para la temperatura
temperatura = temperatura.get_weather()
# crea una variable para la temperatura
temperatura = temperatura.get_temperature('celsius')
# crea una variable para la temperatura
temperatura = temperatura['temp']
# crea una variable para la temperatura
print("La temperatura es: ", temperatura)


# crea una variable para la temperatura
def medicion_temperatura():
    temperatura = temperatura
    if temperatura < 18:
        print("Es muy frio")
    elif temperatura < 25:
        print("Es frio")
    elif temperatura < 30:
        print("Es normal")
    elif temperatura < 35:
        print("Es caluroso")
    elif temperatura < 40:
        print("Es muy caluroso")
    else:
        print("Es muy caluroso")


medicion_temperatura()


# toma datos de la temperatura
def tomar_datos():
    datos = []  # obtiene los datos
    for i in range(5):
        temperatura = owm.weather_at_place(ciudad)
        temperatura = temperatura.get_weather()
        temperatura = temperatura.get_temperature('celsius')
        temperatura = temperatura['temp']
        datos.append(temperatura)
    return datos


# muestra los datos
def mostrar_datos(datos):
    for i in range(5):
        print("Temperatura: ", datos[i])


datos = tomar_datos()
mostrar_datos(datos)


# muestra un mapa geografico con los datos del tiempo
def mostrar_mapa(datos):
    import folium
    import webbrowser
    # crea un mapa
    mapa = folium.Map(location=[-34.603722, -58.381592], zoom_start=12)
    # crea una capa
    capa = folium.FeatureGroup(name="Temperatura")
    # crea un punto
    for i in range(5):
        folium.Marker([-34.603722, -58.381592], popup=datos[i]).add_to(capa)
    # agrega la capa al mapa
    capa.add_to(mapa)
    # muestra el mapa
    mapa.save("temperatura.html")
    # abre el mapa
    webbrowser.open("temperatura.html")


mostrar_mapa(datos)


# muestra un grafico de barras con los datos del tiempo
def mostrar_grafico(datos):
    import matplotlib.pyplot as plt
    # crea una lista
    lista = []
    # crea una lista
    lista2 = []
    # crea una lista
    lista3 = []
    # crea una lista
    lista4 = []
    # crea una lista
    lista5 = []
    # crea una lista
    lista6 = []
    # crea una lista
    lista7 = []
    # crea una lista
    lista8 = []
    # crea una lista
    lista9 = []
    # crea una lista
    lista10 = []
    # crea una lista
    lista11 = []
    # crea una lista
    lista12 = []
    # crea una lista
    lista13 = []
    # crea una lista
    lista14 = []
    # crea una lista
    lista15 = []
    # crea una lista
    lista16 = []
    # crea una lista
    lista17 = []
    # crea una lista
    lista18 = []
    # crea una lista
    lista19 = []
    # crea una lista
    lista20 = []
    # crea una lista
    lista21 = []
    # crea una lista
    lista22 = []
    # crea una lista
    lista23 = []
    # crea una lista
    lista24 = []
    # crea una lista
    lista25 = []
    # crea una lista
    lista26 = []
    # crea una lista
    lista27 = []
    # crea una lista
    lista28 = []
    # crea una lista
    lista29 = []
    # crea una lista
    lista30 = []

    # resume las listas y las muestra todas juntas
    for i in range(5):
        lista.append(datos[i])
    for i in range(5):
        lista2.append(datos[i])
    for i in range(5):
        lista3.append(datos[i])
    for i in range(5):
        lista4.append(datos[i])
    for i in range(5):
        lista5.append(datos[i])
    for i in range(5):
        lista6.append(datos[i])
    for i in range(5):
        lista7.append(datos[i])
    for i in range(5):
        lista8.append(datos[i])
    for i in range(5):
        lista9.append(datos[i])
    for i in range(5):
        lista10.append(datos[i])
    for i in range(5):
        lista11.append(datos[i])
    for i in range(5):
        lista12.append(datos[i])
    for i in range(5):
        lista13.append(datos[i])
    for i in range(5):
        lista14.append(datos[i])
    for i in range(5):
        lista15.append(datos[i])
    for i in range(5):
        lista16.append(datos[i])
    for i in range(5):
        lista17.append(datos[i])
    for i in range(5):
        lista18.append(datos[i])
    for i in range(5):
        lista19.append(datos[i])
    for i in range(5):
        lista20.append(datos[i])
    for i in range(5):
        lista21.append(datos[i])
    for i in range(5):
        lista22.append(datos[i])
    for i in range(5):
        lista23.append(datos[i])
    for i in range(5):
        lista24.append(datos[i])
    for i in range(5):
        lista25.append(datos[i])
    for i in range(5):
        lista26.append(datos[i])
    for i in range(5):
        lista27.append(datos[i])
    for i in range(5):
        lista28.append(datos[i])
    for i in range(5):
        lista29.append(datos[i])
    for i in range(5):
        lista30.append(datos[i])

    # cierra el programa
    plt.close()
    # crea un grafico
    plt.plot(lista, label="1")
    plt.plot(lista2, label="2")
    plt.plot(lista3, label="3")
    plt.plot(lista4, label="4")
    plt.plot(lista5, label="5")
    plt.plot(lista6, label="6")
    plt.plot(lista7, label="7")
    plt.plot(lista8, label="8")
    plt.plot(lista9, label="9")
    plt.plot(lista10, label="10")
    plt.plot(lista11, label="11")
    plt.plot(lista12, label="12")
    plt.plot(lista13, label="13")
    plt.plot(lista14, label="14")
    plt.plot(lista15, label="15")
    plt.plot(lista16, label="16")
    plt.plot(lista17, label="17")
    plt.plot(lista18, label="18")
    plt.plot(lista19, label="19")
    plt.plot(lista20, label="20")
    plt.plot(lista21, label="21")
    plt.plot(lista22, label="22")
    plt.plot(lista23, label="23")
    plt.plot(lista24, label="24")
    plt.plot(lista25, label="25")
    plt.plot(lista26, label="26")
    plt.plot(lista27, label="27")
    plt.plot(lista28, label="28")
    plt.plot(lista29, label="29")
    plt.plot(lista30, label="30")
    plt.legend()
    plt.show()
    # muestra el grafico
    plt.show()
    # se despide del programa
    print("Gracias por usar el programa. Creado por Erick Zanussem")
    # cierra el programa
    plt.close()
