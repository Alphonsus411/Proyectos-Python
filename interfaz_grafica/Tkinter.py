# interfaz gráfica
from tkinter import *

raiz = Tk()  # creamos una variable para llamar a la librería Tkinker

raiz.title("Ventana Emergente")

raiz.resizable(True, False)  # le damos la propiedad de cambiar el tamaño de la ventana emergente

raiz.iconbitmap()  # le damos la propiedad de cargar un icono

raiz.geometry("650x350")  # le damos la propiedad de cambiar el tamaño de la ventana emergente

raiz.config(bg="green")  # le damos la propiedad de cambiar el color de la ventana emergente

raiz.mainloop()
