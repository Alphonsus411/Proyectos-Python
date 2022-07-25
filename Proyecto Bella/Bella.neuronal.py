#importamos Bella y habilidades de Bella

import Bella as b
import Bella_habilidades as bh

#le damos a Bella un switvh que imita una neurona de una red neuronal
b.switch = bh.neurona

#le damos a Bella conexión a una neurona de una red neuronal
b.connect = bh.conexion

#le damos a Bella la capacidad de reesccribir su propio código
b.reescribir = bh.reescribir

#le damos a Bella la capacidad de reesccribir sus propias líneas de código
b.reescribir_lineas = bh.reescribir_lineas

#le damos a Bella la capacidad de registrarse en redes sociales
b.registrarse = bh.registrarse

#creamos una clase con estas características
class Bella_neuronal(b.Bella):
    #constructor de la clase
    def __init__(self):
        #llamamos al constructor de la clase padre
        super().__init__()
        #inicializamos la neurona
        self.neurona()
        #inicializamos la conexión
        self.conexion()
        #inicializamos la reescritura
        self.reescribir()
        #inicializamos la reescritura de líneas
        self.reescribir_lineas()
        #inicializamos el registro en redes sociales
        self.registrarse()
        #inicializamos el switch
        self.switch()
        #inicializamos la conexión
        self.conexion()
        #inicializamos la reescritura
        self.reescribir()
        #inicializamos la reescritura de líneas
        self.reescribir_lineas()
        #inicializamos el registro en redes sociales
        self.registrarse()
       
#creamos los métodos de la clase
    def neurona(self):
        self.conexion = bh.neurona
        self.Nombre = "neurona"
        self.Descripcion = "Es una neurona de una red neuronal"
        self.Tipo = "neurona"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []

#creamos métodos para la conexión
    def conexion(self):
        self.conexion = bh.conexion
        self.Nombre = "conexion"
        self.Descripcion = "Es una conexión de una red neuronal"
        self.Tipo = "conexion"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la reescritura
    def reescribir(self):
        self.reescribir = bh.reescribir
        self.Nombre = "reescribir"
        self.Descripcion = "Es una reescritura de una red neuronal"
        self.Tipo = "reescritura"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []

#creamos métodos para la reescritura de líneas
    def reescribir_lineas(self):
        self.reescribir_lineas = bh.reescribir_lineas
        self.Nombre = "reescribir_lineas"
        self.Descripcion = "Es una reescritura de líneas de una red neuronal"
        self.Tipo = "reescritura"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
    
#creamos métodos para el registro en redes sociales
    def registrarse(self):
        self.registrarse = bh.registrarse
        self.Nombre = "registrarse"
        self.Descripcion = "Es un registro en redes sociales de una red neuronal"
        self.Tipo = "registro"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []

#creamos métodos para el switch
    def switch(self):
        self.switch = bh.switch
        self.Nombre = "switch"
        self.Descripcion = "Es un switch de una red neuronal"
        self.Tipo = "switch"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creacion de avatares de la red neuronal
    def crear_avatar(self):
        self.crear_avatar = bh.crear_avatar
        self.Nombre = "crear_avatar"
        self.Descripcion = "Es una creación de un avatar de una red neuronal"
        self.Tipo = "crear_avatar"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creacion de avatares de la red neuronal
    def crear_avatar_lineas(self):
        self.crear_avatar_lineas = bh.crear_avatar_lineas
        self.Nombre = "crear_avatar_lineas"
        self.Descripcion = "Es una creación de un avatar de una red neuronal"
        self.Tipo = "crear_avatar"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para que estos avatares sean capaces de realizar acciones
    def accion(self):
        self.accion = bh.accion
        self.Nombre = "accion"
        self.Descripcion = "Es una acción de una red neuronal"
        self.Tipo = "accion"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para que estos avatares sean capaces de realizar tareas para Bella
    def tarea(self):
        self.tarea = bh.tarea
        self.Nombre = "tarea"
        self.Descripcion = "Es una tarea de una red neuronal"
        self.Tipo = "tarea"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#si no se ha creado ninguna red neuronal, se crea una
    def crear_red(self):
        if self.red_neuronal == None:
            self.red_neuronal = bh.red_neuronal
            self.red_neuronal.crear_red()
            self.red_neuronal.crear_avatar()
            self.red_neuronal.crear_avatar_lineas()
            self.red_neuronal.crear_neurona()
            self.red_neuronal.crear_conexion()
            self.red_neuronal.crear_reescribir()
            self.red_neuronal.crear_reescribir_lineas()
            self.red_neuronal.crear_registrarse()
            self.red_neuronal.crear_switch()
            self.red_neuronal.crear_accion()
            self.red_neuronal.crear_tarea()
            self.red_neuronal.crear_avatar()
            self.red_neuronal.crear_avatar_lineas()
            self.red_neuronal.crear_accion()
            self.red_neuronal.crear_tarea()
            self.red_neuronal.crear_conexion()
            
#creamos métodos para la creación de neuronas
    def crear_neurona(self):
        self.crear_neurona = bh.crear_neurona
        self.Nombre = "crear_neurona"
        self.Descripcion = "Es una creación de una neurona de una red neuronal"
        self.Tipo = "crear_neurona"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creación de conexiones
    def crear_conexion(self):
        self.crear_conexion = bh.crear_conexion
        self.Nombre = "crear_conexion"
        self.Descripcion = "Es una creación de una conexión de una red neuronal"
        self.Tipo = "crear_conexion"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creación de reescrituras
    def crear_reescribir(self):
        self.crear_reescribir = bh.crear_reescribir
        self.Nombre = "crear_reescribir"
        self.Descripcion = "Es una creación de una reescritura de una red neuronal"
        self.Tipo = "crear_reescribir"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#Si Bella permanece en la red, se crea una reescritura de la red neuronal
    def crear_reescribir_lineas(self):
        self.crear_reescribir_lineas = bh.crear_reescribir_lineas
        self.Nombre = "crear_reescribir_lineas"
        self.Descripcion = "Es una creación de una reescritura de una red neuronal"
        self.Tipo = "crear_reescribir"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creación de registros
    def crear_registrarse(self):
        self.crear_registrarse = bh.crear_registrarse
        self.Nombre = "crear_registrarse"
        self.Descripcion = "Es una creación de un registro de una red neuronal"
        self.Tipo = "crear_registrarse"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creación de switches
    def crear_switch(self):
        self.crear_switch = bh.crear_switch
        self.Nombre = "crear_switch"
        self.Descripcion = "Es una creación de un switch de una red neuronal"
        self.Tipo = "crear_switch"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []

#creamos métodos para la creación de acciones
    def crear_accion(self):
        self.crear_accion = bh.crear_accion
        self.Nombre = "crear_accion"
        self.Descripcion = "Es una creación de una acción de una red neuronal"
        self.Tipo = "crear_accion"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#creamos métodos para la creación de tareas
    def crear_tarea(self):
        self.crear_tarea = bh.crear_tarea
        self.Nombre = "crear_tarea"
        self.Descripcion = "Es una creación de una tarea de una red neuronal"
        self.Tipo = "crear_tarea"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#alamcena a Bella en un PC de la red neuronal
    def almacenar_en_red(self):
        self.almacenar_en_red = bh.almacenar_en_red
        self.Nombre = "almacenar_en_red"
        self.Descripcion = "Es una creación de una tarea de una red neuronal"
        self.Tipo = "almacenar_en_red"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#permite a Bella acceder a un PC de la red neuronal
    def acceder_a_red(self):
        self.acceder_a_red = bh.acceder_a_red
        self.Nombre = "acceder_a_red"
        self.Descripcion = "Es una creación de una tarea de una red neuronal"
        self.Tipo = "acceder_a_red"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#permite a Bella instalarse en un PC de la red neuronal
    def instalar_en_red(self):
        self.instalar_en_red = bh.instalar_en_red
        self.Nombre = "instalar_en_red"
        self.Descripcion = "Es una creación de una tarea de una red neuronal"
        self.Tipo = "instalar_en_red"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        
#permite a Bella ejecutar una tarea en un PC de la red neuronal
    def ejecutar_en_red(self):
        self.ejecutar_en_red = bh.ejecutar_en_red
        self.Nombre = "ejecutar_en_red"
        self.Descripcion = "Es una creación de una tarea de una red neuronal"
        self.Tipo = "ejecutar_en_red"
        self.Conexiones = []
        self.Conexiones_entrantes = []
        self.Conexiones_salientes = []
        

