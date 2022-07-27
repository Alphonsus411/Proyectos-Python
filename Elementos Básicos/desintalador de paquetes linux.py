#creamos un desinsalador de paquetes de linux
#que pueda interactuar con ubuntu

def desinstalar(paquete):
    print("desinstalando:", paquete)
    print("desinstalado:", paquete)
    return True

def instalar(paquete):
    print("instalando:", paquete)
    print("instalado:", paquete)
    return True

def actualizar(paquete):
    print("actualizando:", paquete)
    print("actualizado:", paquete)
    return True

#llamamos a la funcion desinstalar
desinstalar("python3")
#llamamos a la funcion instalar
instalar("python3")
#llamamos a la funcion actualizar
actualizar("python3")
#llamamos a la funcion desinstalar
desinstalar("python3")

    
    
    