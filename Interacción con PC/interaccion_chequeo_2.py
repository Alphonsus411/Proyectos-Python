#!/usr/bin/env python3

"""Importe el módulo de solicitud en el archivo mediante las instrucciones de importación.
Para comprobar si el host local está configurado correctamente, utilizamos el módulo socket.
A continuación, escriba una función check_localhost, que comprueba si el host local está configurado correctamente. Hacemos esto llamando al gethostbyname dentro de la función.

localhost = socket.gethostbyname('localhost')

La función anterior traduce un nombre de host al formato de dirección IPv4. Pase el parámetro localhost a la función gethostbyname. El resultado de esta función debe ser 127.0.0.1.
Edite la función check_localhost para que devuelva true si la función devuelve 127.0.0.1.
Ahora, escribiremos otra función llamada check_connectivity. Esto comprueba si el equipo puede realizar llamadas correctas a Internet.
Una solicitud es cuando hace ping a un sitio web para obtener información. La biblioteca de solicitudes está diseñada para esta tarea. Utilizará el módulo de solicitud para esto y llamará al método GET pasando http://www.google.com como parámetro.

request = requests.get("http://www.google.com")

Esto devuelve el código de estado del sitio web. Este código de estado es un valor entero. Ahora, asigne el resultado a una variable de respuesta y verifique el atributo status_code de esa variable. Debería devolver 200.
Edite la función check_connectivity para que devuelva true si la función devuelve 200 status_code"""

import socket
import requests

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True

def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request
    if response.status_code == 200:
        return True

print(check_localhost())
print(check_connectivity())

# Path: Elementos Básicos\interaccion_chequeo_3.py
