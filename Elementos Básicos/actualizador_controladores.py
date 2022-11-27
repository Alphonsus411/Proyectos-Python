"""
Creamos un actualizador de controladores para el sistema de controladores del PC, 
el cual interactúe con windows y permita detectar errores y depurarlos.

"""

import os
import sys
import time
import subprocess
import win32com.client


# Creamos una clase para el actualizador de controladores
class ActualizadorControladores:
    def __init__(self):
        self.controladores = win32com.client.Dispatch("SystemInfo.SystemInfo")
        self.controladores.Refresh()
        self.controladores = self.controladores.GetControllers()

    def listar_controladores(self):
        print("Controladores del sistema:")
        for controlador in self.controladores:
            print("Controlador: ", controlador.Name)
            print("Estado: ", controlador.Status)
            print("Tipo: ", controlador.Type)
            print("Fabricante: ", controlador.Manufacturer)
            print("Versión: ", controlador.Version)
            print("Fecha: ", controlador.Date)
            print("")

    def actualizar_controladores(self):
        print("Actualizando controladores...")
        for controlador in self.controladores:
            if controlador.Status == "Error":
                print("Actualizando controlador: ", controlador.Name)
                controlador.Update()
                print("Controlador actualizado: ", controlador.Name)
                print("")
                
# Creamos un objeto de la clase
actualizador = ActualizadorControladores()

# Listamos los controladores
actualizador.listar_controladores()

# Actualizamos los controladores
actualizador.actualizar_controladores()

# Detectamos errores en los controladores
actualizador.listar_controladores()

# Fin del programa
