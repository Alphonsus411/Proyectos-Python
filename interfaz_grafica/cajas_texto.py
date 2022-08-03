# uso de label

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=800, height=300)
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, sticky="e", padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, sticky="e", padx=10, pady=10)
cuadroApellido.config(fg="blue", justify="center")
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, sticky="e", padx=10, pady=10)
cuadroDireccion.config(fg="green", justify="center")
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")
cuadroComentario = Text(miFrame, width=16, height=5)  # generamos un cuadro de texto grande
cuadroComentario.grid(row=4, column=1, padx=10, pady=10)  # posicionamos el cuadro de texto
scrollVertical = Scrollbar(miFrame, command=cuadroComentario.yview())  # generamos un Scroll vertical para el cuadro de
# texto
scrollVertical.grid(row=4, column=2, sticky="nsew")  # llamamos y posicionamos el scroll bar usando "nsew" para darle
# el tamaño del cuadro de texto
cuadroComentario.config(yscrollcommand=scrollVertical.set)  # fijamos las propiedades del scroll bar
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
comentarioLabel = Label(miFrame, text="Comentario: ")  # generamos el comentario del cuadro de texto
comentarioLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)  # le damos dimensiones

raiz.mainloop()
