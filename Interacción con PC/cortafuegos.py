"""
Creamos un cortafuegos para nuestra conexión de internet habitual mediante
un script de python, que evite que terceras personas puedan hackear nuestra conexión

"""

import os
import sys

# Comprobamos que el usuario es root
if os.getuid() != 0:
    print ("Debes ser root para ejecutar este script")
    sys.exit(1)
    
# Comprobamos que el usuario ha introducido un parámetro
if len(sys.argv) != 2:
    print ("Debes introducir un parámetro")
    sys.exit(1)
    
# Comprobamos que el parámetro introducido es correcto
if sys.argv[1] != "on" and sys.argv[1] != "off":
    print ("Debes introducir on o off")
    sys.exit(1)
    
# Comprobamos si el cortafuegos está activado o no
if sys.argv[1] == "on":
    # Activamos el cortafuegos
    os.system("iptables -P INPUT DROP")
    os.system("iptables -P OUTPUT DROP")
    os.system("iptables -P FORWARD DROP")
    os.system("iptables -A INPUT -i lo -j ACCEPT")
    os.system("iptables -A OUTPUT -o lo -j ACCEPT")
    os.system("iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
    os.system("iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT")
    print ("Cortafuegos activado")
else:
    # Desactivamos el cortafuegos
    os.system("iptables -F")
    os.system("iptables -X")
    os.system("iptables -Z")
    os.system("iptables -t nat -F")
    os.system("iptables -t nat -X")
    os.system("iptables -t nat -Z")
    os.system("iptables -t mangle -F")
    os.system("iptables -t mangle -X")
    os.system("iptables -t mangle -Z")
    print ("Cortafuegos desactivado")
    
sys.exit(0)

# Ejecutamos el script con el parámetro on
# python cortafuegos.py on

# Ejecutamos el script con el parámetro off
# python cortafuegos.py off

# Comprobamos que el cortafuegos está activado
# iptables -L

# Comprobamos que el cortafuegos está desactivado
# iptables -L



