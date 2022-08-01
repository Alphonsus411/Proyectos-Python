# uso de label

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, height=400, width=500)
miFrame.pack()

miImagen = PhotoImage(file="imagenes/linux.png")
# una imagen desde un directorio
Label(miFrame, text="Esto es un Label", fg="green", font=("Arial", 20)).place(x=100, y=200)
Label(miFrame, image=miImagen).place(x=100, y=100)  # ajustamos el tamaño de la
# ventana, juntamos dos
# descriptores de método en uno solo

raiz.mainloop()  # llamamos al label con este método
