"""
Vamos a crear una protección de wifi que detecte la intrusión de terceros y cierre la conexión para estos intrusos.

"""

import subprocess
import time
import os

# Definimos la dirección MAC de nuestro dispositivo
mac = "D0-37-45-1A-B1-99"

# Definimos la dirección MAC de nuestro router
router = "e0-41-36-3a-02-e8"

# buscamos en la lista de dispositivos conectados a la red la dirección MAC de nuestro dispositivo
def buscar():
    # ejecutamos el comando de terminal para ver los dispositivos conectados a la red
    # y lo guardamos en una variable
    dispositivos = subprocess.check_output(["arp", "-a"])
    # buscamos la dirección MAC de nuestro dispositivo en la lista de dispositivos conectados
    if mac in str(dispositivos):
        # si la encuentra, devuelve True
        return True
    else:
        # si no la encuentra, devuelve False
        return False
    
# si la dirección MAC de nuestro dispositivo no está en la lista de dispositivos conectados
# significa que alguien más se ha conectado a la red
# por lo tanto, cerramos la conexión para este intruso
def cerrar():
    # ejecutamos el comando de terminal para cerrar la conexión para este intruso, habilitando la elevacion
    os.system("netsh wlan disconnect interface=\"Wi-Fi\"")
    # ejecutamos el comando de terminal para volver a conectar nuestro dispositivo a la red
    os.system("netsh wlan connect name=\"MiWiFi\"")
    # ejecutamos el comando de terminal para ver los dispositivos conectados a la red
    # y lo guardamos en una variable
    dispositivos = subprocess.check_output(["arp", "-a"])
    # buscamos la dirección MAC de nuestro dispositivo en la lista de dispositivos conectados
    if mac in str(dispositivos):
        # si la encuentra, devuelve True
        return True
    
# bucle infinito
while True:
    # si la dirección MAC de nuestro dispositivo no está en la lista de dispositivos conectados
    if not buscar():
        # cerramos la conexión para este intruso
        cerrar()
    # esperamos 10 segundos
    time.sleep(10)
    


