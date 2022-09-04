#! usr/bin/env python3

import shutil
import psutil


def check_disk_usage(disk):  # funcion para comprobación del disco del PC con condicionales derivadas de la librería
    # shutil
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():  # función para comprobación del uso de la CPU y si presenta problemas de rendimiento usando
    # psutil
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage(): # llamada a las dos funciones de chequeo y alerta de mensaje
    # de error en el funcionamiento del sistema
    print("Error en sistema")
else:
    print("Funcionamiento correcto, fin de la comprobación")


