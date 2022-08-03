# botones en la interfaz

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=800, height=300)
miFrame.pack()
miNombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=miNombre)  # asociamos con la funcion del boton y el parámetro miNombre
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
cuadroComentario = Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=4, column=1, padx=10, pady=10)
scrollVertical = Scrollbar(miFrame, command=cuadroComentario.yview)  # crea la característica del ScrollBar
scrollVertical.grid(row=4, column=2, sticky="nsew")  # sitúa el Scrollbar en posición vertical
cuadroComentario.config(yscrollcommand=scrollVertical.set)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=1)
direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
comentarioLabel = Label(miFrame, text="Comentario: ")  # texto para la funcionalidad del comentario
comentarioLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)  # características del comentario y su


# posicionamiento espacial

def codigoBoton(self):  # funcion para el boton del cuestionario
    miNombre.set("Erick")


botonEnvio = Button(raiz, text="Enviar: ",
                    command=codigoBoton)  # creamos un boton interactivo en la página de formulario
botonEnvio.pack()  # llamamos al boton para imprimirlo en pantalla

raiz.mainloop()
