#generamos un programa que componga musica a partir de una lista de canciones
#que analice archivos mp3
#que reconoosca canciones en español
#que pueda crear pistas mezclando canciones
#que pueda reproducir canciones
#que pueda reproducir canciones y filtrar por artista
#que pueda reproducir canciones y filtrar por album
#que pueda reproducir canciones y filtrar por genero
#que pueda reproducir canciones y filtrar por año
#que pueda reproducir canciones y filtrar por duracion
#que pueda reproducir canciones y filtrar por calidad
#que alamacene canciones en una base de datos

constructor = __import__('constructor')
reconocedor = __import__('reconocedor')
reproductor = __import__('reproductor')
filtrador = __import__('filtrador')
almacenador = __import__('almacenador')
reproductor = __import__('reproductor')


def main():
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = []
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = constructor.consultar_youtube()
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = reconocedor.reconocer_canciones(canciones)
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = filtrador.filtrar_canciones(canciones)
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = almacenador.almacenar_canciones(canciones)
    #   creamos una lista de canciones consultadas en youtube
    #   que contenga canciones de la lista de canciones
    canciones = reproductor.reproducir_canciones(canciones)
    
#en base a esa lista, clasificamos las canciones
#en una lista de canciones por artista
#en una lista de canciones por album
#en una lista de canciones por genero
#en una lista de canciones por año
#en una lista de canciones por duracion
#en una lista de canciones por calidad

canciones = []

def clasificar():
    for i in range(len(canciones, 1)):
        if canciones[i].artista == canciones[i+1].artista:
            canciones[i].artista = canciones[i+1].artista
        else:
            canciones[i].artista = canciones[i+1].artista
        if canciones[i].artista == "":
            canciones[i].artista = "Desconocido"
        if canciones[i].album == "":
            canciones[i].album = "Desconocido"
        if canciones[i].genero == "":
            canciones[i].genero = "Desconocido"
        if canciones[i].año == "":
            canciones[i].año = "Desconocido"
        if canciones[i].duracion == "":
            canciones[i].duracion = "Desconocido"
        if canciones[i].calidad == "":
            canciones[i].calidad = "Desconocido"
    else:
        print("No hay canciones")
        
#despues, en base a esas canciones, escogemos una cancion
#para reproducir
def reproducir():
    print("Reproduciendo canciones")
    for i in range(len(canciones, 1)):
        print("Cancion: " + canciones[i].nombre)
        print("Artista: " + canciones[i].artista)
        print("Album: " + canciones[i].album)
        print("Genero: " + canciones[i].genero)
        print("Año: " + canciones[i].año)
        print("Duracion: " + canciones[i].duracion)
        print("Calidad: " + canciones[i].calidad)
        print("\n")
    else:
        print("No hay canciones")
        


    
        
        


    