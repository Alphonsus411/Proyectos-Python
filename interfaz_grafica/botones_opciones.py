from tkinter import *

raiz = Tk()

opcion = IntVar()  # creamos la opcion para poder seleccionar botones


def imprimir():  # creamos una funcion para poder guardar el valor seleccionado
    if opcion.get() == 1:
        etiqueta.config(text="Has elegido masculino")
    else:
        etiqueta.config(text="Has elegido femenino")


Label(raiz, text="Seleccione su género: ").pack()

Radiobutton(raiz, text="Masculino", variable=opcion, value=1, command=imprimir).pack()  # opcion masculino para el
# boton
Radiobutton(raiz, text="Femenino", variable=opcion, value=2, command=imprimir).pack()  # opcion femenino para el boton

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()
