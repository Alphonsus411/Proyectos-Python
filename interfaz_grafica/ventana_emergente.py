# ventanas emergentes

from tkinter import *
from tkinter import messagebox  # propiedad de ventanas emergentes
from tkinter import filedialog  # propiedad de la ventana de diálogo

raiz = Tk()


def infoAdicional():  # con esta funcion invocamos la utilidad de la ventana emergente
    messagebox.showinfo("Programa de Erick Zanussem", "Licencia de Código Abierto")


def infoLicencia():
    messagebox.showwarning("Licencia", "Libre Uso")


def salirApp():
    valor = messagebox.askokcancel("Salir", "¿Estás seguro que deseas salir?")
    if valor == True:
        raiz.destroy()


def abreArchivo():
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="/",
                                         filetypes=(("fichero de texto", "*.txt"), ("fichero de excel", "*.xlsx"))  # parámetros para abrir un archivo
    # del directorio, puede ser .txt, .doc, .xslx, etcétera
    print(archivo)


def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")
    if valor == False:
        raiz.destroy()


barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreArchivo)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirApp)

edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")

herramientaMenu = Menu(barraMenu, tearoff=0)
herramientaMenu.add_command(label="Reemplazar")

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=infoLicencia)  # llamamos a las propiedades de la ventana emergente
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)  # cada una de sus propiedades separada
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()
