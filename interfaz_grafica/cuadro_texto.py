# uso de label

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=800, height=300)  # este frame cambia el contenido de la caja de diálogo
miFrame.pack()

cuadroNombre = Entry(miFrame)  # creamos un cuadro de texto con registro de entrada
# cuadroTexto.place(x=100, y=100)  # posicionamiento 100 pixel a la izquierda, 100 a la derecha
cuadroNombre.grid(row=0, column=1, sticky="e", padx=10, pady=10)  # damos parámetros de posicionamiento
cuadroNombre.config(fg="red", justify="center")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, sticky="e", padx=10, pady=10)  # pady, posicionamiento vertical
cuadroApellido.config(fg="blue", justify="center")
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, sticky="e", padx=10, pady=10)
cuadroDireccion.config(fg="green", justify="center")
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

nombreLabel = Label(miFrame, text="Nombre: ")  # cuadro de texto del Label
# nombreLabel.place(x=100, y=100)  # coordenadas del Label
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0,  sticky="e", padx=10, pady=10)  # respetamos,  la fila, pero saltamos una columna
# con el
# término row
direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)


raiz.mainloop()
