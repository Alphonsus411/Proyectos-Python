#creamos un programa de gestion de usuarios
#importamos los modulos necesarios

import os
import sys
import getpass
import time
import datetime
import subprocess
import re
import shutil
import smtplib
import socket
import urllib.request
import http.client
import ftplib
import ssl
import hashlib
import base64
import random
import string
import requests
import json
import urllib.parse
import urllib.error

#creamos una funcion para pedir el nombre de usuario
def pedir_nombre_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    return nombre_usuario

#creamos una funcion para pedir la contraseña
def pedir_contraseña():
    contraseña = getpass.getpass("Introduce tu contraseña: ")
    return contraseña

#creamos una funcion para pedir el nombre
def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre

#creamos una funcion para pedir el apellido
def pedir_apellido():
    apellido = input("Introduce tu apellido: ")
    return apellido

#creamos una funcion para pedir el email
def pedir_email():
    email = input("Introduce tu email: ")
    return email

#creamos una funcion para pedir el telefono
def pedir_telefono():
    telefono = input("Introduce tu telefono: ")
    return telefono

#creamos una funcion para pedir la direccion
def pedir_direccion():
    direccion = input("Introduce tu direccion: ")
    return direccion

#creamos una funcion para pedir la fecha de nacimiento
def pedir_fecha_nacimiento():
    fecha_nacimiento = input("Introduce tu fecha de nacimiento: ")
    return fecha_nacimiento

#creamos una funcion para pedir la fecha de alta
def pedir_fecha_alta():
    fecha_alta = input("Introduce tu fecha de alta: ")
    return fecha_alta

#creamos una funcion para pedir el tipo de usuario
def pedir_tipo_usuario():
    tipo_usuario = input("Introduce tu tipo de usuario: ")
    return tipo_usuario

#creamos una funcion para alamcenar los datos de los usuarios
def almacenar_datos_usuarios(nombre_usuario, contraseña, nombre, apellido, email, telefono, direccion, fecha_nacimiento, fecha_alta, tipo_usuario):
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "a")
    #escribimos los datos de los usuarios en el archivo
    datos_usuarios.write(nombre_usuario + "," + contraseña + "," + nombre + "," + apellido + "," + email + "," + telefono + "," + direccion + "," + fecha_nacimiento + "," + fecha_alta + "," + tipo_usuario + "\n")
    #cerramos el archivo
    datos_usuarios.close()
    
#creamos una funcion para gestionar los datos en el archivo
def gestionar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para mostrar los datos de los usuarios
def mostrar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para eliminar los datos de los usuarios
def eliminar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #cerramos el archivo
    datos_usuarios.close()

#creamos un gestor de datos de usuarios
def gestionar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()
    
#creamos una funcion para clasificar los datos de los usuarios
def clasificar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()
    
#creamos una funcion para buscar los datos de los usuarios
def buscar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para modificar los datos de los usuarios
def modificar_datos_usuarios():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para crear un usuario
def crear_usuario():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()
    
#creamos una funcion para eliminar un usuario
def eliminar_usuario():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para crear una cuenta
def crear_cuenta():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para eliminar una cuenta
def eliminar_cuenta():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para iniciar sesion
def iniciar_sesion():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para cerrar sesion
def cerrar_sesion():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para cambiar contraseña
def cambiar_contrasena():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para integrar todos los datos en excel y guardarlos en un archivo
def integrar_datos():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para integrar todos los datos en excel y guardarlos en un archivo
def integrar_datos_excel():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para depurar los datos en excel y ordenarlos en un archivo
def depurar_datos():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para depurar los datos en excel y ordenarlos en un archivo
def depurar_datos_excel():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para imprimir los datos en word y guardarlos en un archivo
def imprimir_datos():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una funcion para imprimir los datos en word y guardarlos en un archivo
def imprimir_datos_word():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#creamos una interfaz de almecenamiento de datos
def almacenamiento_datos():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()

#protegemos y encriptamos los datos
def proteger_datos():
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "r")
    #leemos los datos de los usuarios del archivo
    datos_usuarios_leidos = datos_usuarios.readlines()
    #cerramos el archivo
    datos_usuarios.close()
    #creamos una variable para almacenar los datos de los usuarios
    datos_usuarios = open("datos_usuarios.txt", "w")
    #escribimos los datos de los usuarios en el archivo
    for linea in datos_usuarios_leidos:
        print(linea)
        datos_usuarios.write(linea)
    #cerramos el archivo
    datos_usuarios.close()
    
#creamos un menu de opciones
def menu():
    print("1. Depurar datos")
    print("2. Depurar datos en excel")
    print("3. Imprimir datos")
    print("4. Imprimir datos en word")
    print("5. Almacenar datos")
    print("6. Proteger datos")
    print("7. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        depurar_datos()
    elif opcion == 2:
        depurar_datos_excel()
    elif opcion == 3:
        imprimir_datos()
    elif opcion == 4:
        imprimir_datos_word()
    elif opcion == 5:
        almacenamiento_datos()
    elif opcion == 6:
        proteger_datos()
    elif opcion == 7:
        print("Gracias por usar nuestro programa")
        exit()
    else:
        print("Opcion no valida")
        menu()
    
    #cerramos el programa y salimos
    exit()
    
    





