# frames

from tkinter import *

raiz = Tk()
raiz.title("Ventana Emergente")
# raiz.resizable(True, False)
raiz.iconbitmap("")
# raiz.geometry("650x350")
raiz.config(bg="green")

miFrame = Frame()
# miFrame.pack(side="left", anchor="s")  # ubicación de la ventana interior
miFrame.pack(fill="x", expand=1)
miFrame.config(bg="red")  # color de la ventana externa
miFrame.config(width="650", height="350")  # dimensiones de la ventana externa
miFrame.config(bd=35)  # le damos un tamaño a la ventana interna
miFrame.config(relief="groove")  # creamos un borde para la ventana
miFrame.config(cursor="pirate")  # cambiamos el cursor dentro de la ventana


raiz.mainloop()
