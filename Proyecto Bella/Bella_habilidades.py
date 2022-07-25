#importamos Bella
from gettext import install
from Bella import *

#buscamos las librerias compatibles con el sistema
import os
import sys
import time
import datetime
import random
import subprocess
import threading
import multiprocessing
import signal
import json
import re
import urllib.request
import urllib.parse
import urllib.error

#instalamos el numpy 
import numpy as np
#instalamos el matplotlib 
import matplotlib.pyplot as plt
#instalamos ntlk en modo compatible
install = np.__import__('ntlk',fromlist=['word_tokenize'])
#instalamos el pandas en modo compatible
install = np.__import__('pandas',fromlist=['read_csv'])
#instalamos el sklearn en modo compatible
install = np.__import__('sklearn',fromlist=['linear_model'])
#instalamos Quiskit en modo compatible
install = np.__import__('qiskit',fromlist=['QuantumCircuit'])
#instalamos el scikit-learn en modo compatible
install = np.__import__('sklearn',fromlist=['linear_model'])
#instalamos acceso a wikipedia en modo compatible
install = np.__import__('wikipedia',fromlist=['summary'])
#instalamos el pyttsx3 en modo compatible
install = np.__import__('pyttsx3',fromlist=['speak'])
#instalamos el speech_recognition en modo compatible
install = np.__import__('speech_recognition',fromlist=['recognize_google'])
#instalamos el pyaudio en modo compatible
install = np.__import__('pyaudio',fromlist=['PyAudio'])
#instalamos el pyttsx3 en modo compatible
install = np.__import__('pyttsx3',fromlist=['speak'])

#damos a Bella una clase que hereda de la clase padre Bella
class Bella_habilidades(Bella):
    #constructor de la clase
    def __init__(self):
        #llamamos al constructor de la clase padre
        super().__init__()
        #inicializamos las variables de la clase
        self.__habilidades = []
        self.__habilidades_nombre = []
        self.__habilidades_descripcion = []
        self.__habilidades_imagen = []
        
    #metodo para obtener las habilidades
    def get_habilidades(self):
        #devuelve las habilidades
        return self.__habilidades

    #metodo para obtener los nombres de las habilidades
    def get_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__habilidades_nombre
    #metodo para obtener las descripciones de las habilidades
    def get_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__habilidades_descripcion
    #metodo para obtener las imagenes de las habilidades
    def get_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__habilidades_imagen
    #metodo para obtener la cantidad de habilidades
    def get_cantidad_habilidades(self):
        #devuelve la cantidad de habilidades
        return len(self.__habilidades)
    
#definimos patrones para la busqueda de habilidades
patron_habilidades = re.compile(r'(?<=<div class="habilidades">).*?(?=</div>)',re.DOTALL)
patron_habilidades_nombre = re.compile(r'(?<=<h3>).*?(?=</h3>)',re.DOTALL)
patron_habilidades_descripcion = re.compile(r'(?<=<p>).*?(?=</p>)',re.DOTALL)
patron_habilidades_imagen = re.compile(r'(?<=<img src=").*?(?=" alt=")',re.DOTALL)

#definimos una clase para la busqueda de habilidades
class Busqueda_habilidades():
    #constructor de la clase
    def __init__(self):
        #inicializamos las variables de la clase
        self.__habilidades = []
        self.__habilidades_nombre = []
        self.__habilidades_descripcion = []
        self.__habilidades_imagen = []
        
    # metodo para obtener las habilidades
    def get_habilidades(self):
        #devuelve las habilidades
        return self.__habilidades

    # metodo para obtener los nombres de las habilidades
    def get_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__habilidades_nombre
    
    # metodo para obtener las descripciones de las habilidades
    def get_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__habilidades_descripcion
    # metodo para obtener las imagenes de las habilidades
    def get_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__habilidades_imagen

# damos a Bella la capacidad de tomar datos de una pagina web
class Bella_habilidades_web(Bella_habilidades):
    #constructor de la clase
    def __init__(self):
        #llamamos al constructor de la clase padre
        super().__init__()
        #inicializamos las variables de la clase
        self.__habilidades = []
        self.__habilidades_nombre = []
        self.__habilidades_descripcion = []
        self.__habilidades_imagen = []
        self.__url = ''
        self.__html = ''
        self.__busqueda = Busqueda_habilidades()
        self.__busqueda_habilidades = Busqueda_habilidades()
        self.__busqueda_habilidades_nombre = Busqueda_habilidades()
        self.__busqueda_habilidades_descripcion = Busqueda_habilidades()
        self.__busqueda_habilidades_imagen = Busqueda_habilidades()
        
    
    #metodo para obtener la url de la pagina web
    def get_url(self):
        #devuelve la url de la pagina web
        return self.__url
    #metodo para obtener las habilidades
    def get_habilidades(self):
        #devuelve las habilidades
        return self.__habilidades
    #metodo para obtener los nombres de las habilidades
    def get_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__habilidades_nombre
    #metodo para obtener las descripciones de las habilidades
    def get_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__habilidades_descripcion
    #metodo para obtener las imagenes de las habilidades
    def get_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__habilidades_imagen
    #metodo para obtener la busqueda de habilidades
    def get_busqueda(self):
        #devuelve la busqueda de habilidades
        return self.__busqueda
    
    #metodo para obtener el html de la pagina web
    def get_html(self):
        #devuelve el html de la pagina web
        return self.__html
    
    #metodo para obtener las habilidades
    def get_busqueda_habilidades(self):
        #devuelve las habilidades
        return self.__busqueda_habilidades
    #metodo para obtener los nombres de las habilidades
    def get_busqueda_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__busqueda_habilidades_nombre
    #metodo para obtener las descripciones de las habilidades
    def get_busqueda_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__busqueda_habilidades_descripcion
    #metodo para obtener las imagenes de las habilidades
    def get_busqueda_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__busqueda_habilidades_imagen
    #metodo para obtener la busqueda de habilidades

# damos a Bella la capacidad de tomar datos de wikipedia
class Bella_habilidades_wikipedia(Bella_habilidades):
    #constructor de la clase
    def __init__(self):
        #llamamos al constructor de la clase padre
        super().__init__()
        #inicializamos las variables de la clase
        self.__habilidades = []
        self.__habilidades_nombre = []
        self.__habilidades_descripcion = []
        self.__habilidades_imagen = []
        self.__url = ''
        self.__html = ''
        self.__busqueda = Busqueda_habilidades()
        self.__busqueda_habilidades = Busqueda_habilidades()
        self.__busqueda_habilidades_nombre = Busqueda_habilidades()
        self.__busqueda_habilidades_descripcion = Busqueda_habilidades()
        self.__busqueda_habilidades_imagen = Busqueda_habilidades()
        
    #metodo para obtener la url de la pagina web
    def get_url(self):
        #devuelve la url de la pagina web
        return self.__url
    #metodo para obtener las habilidades
    def get_habilidades(self):
        #devuelve las habilidades
        return self.__habilidades
    #metodo para obtener los nombres de las habilidades
    def get_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__habilidades_nombre
    #metodo para obtener las descripciones de las habilidades
    def get_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__habilidades_descripcion
    #metodo para obtener las imagenes de las habilidades
    def get_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__habilidades_imagen
    #metodo para obtener la busqueda de habilidades
    def get_busqueda(self):
        #devuelve la busqueda de habilidades
        return self.__busqueda
    #metodo para obtener el html de la pagina web
    def get_html(self):
        #devuelve el html de la pagina web
        return self.__html
    #metodo para obtener las habilidades
    def get_busqueda_habilidades(self):
        #devuelve las habilidades
        return self.__busqueda_habilidades
    #metodo para obtener los nombres de las habilidades
    def get_busqueda_habilidades_nombre(self):
        #devuelve los nombres de las habilidades
        return self.__busqueda_habilidades_nombre
    #metodo para obtener las descripciones de las habilidades
    def get_busqueda_habilidades_descripcion(self):
        #devuelve las descripciones de las habilidades
        return self.__busqueda_habilidades_descripcion
    #metodo para obtener las imagenes de las habilidades
    def get_busqueda_habilidades_imagen(self):
        #devuelve las imagenes de las habilidades
        return self.__busqueda_habilidades_imagen
    
   


    


        
    


    

