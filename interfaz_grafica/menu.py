# menu

from tkinter import *

raiz = Tk()

barraMenu = Menu(raiz)  # creamos un menu
raiz.config(menu=barraMenu, width=300, height=300)  # configuramos sus dimensiones

archivoMenu = Menu(barraMenu, tearoff=0)  # propiedades del menu, una por una
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")  # añadimos comandos del submenu
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() # separa los departamentos del submenu con este comando
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu = Menu(barraMenu, tearoff=0)
herramientaMenu.add_command(label="Reemplazar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)  # cada una de sus propiedades separada
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()
