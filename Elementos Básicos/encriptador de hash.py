# crea un encriptador de hash
def encriptador():
    import hashlib
    print("Escribe un mensaje para encriptar:")
    mensaje = input()
    mensaje = mensaje.encode('utf-8')
    hash = hashlib.sha256(mensaje).hexdigest()
    print("El mensaje encriptado es:")
    print(hash)

    print("Escribe un mensaje para desencriptar:")
    mensaje = input()
    mensaje = mensaje.encode('utf-8')
    hash = hashlib.sha256(mensaje).hexdigest()
    print("El mensaje desencriptado es:")
    print(hash)


# llama a la función
encriptador()
# ejecuta el programa
if __name__ == "__main__":
    encriptador()

# finaliza el programa
print("Fin del programa")
# se cierra el programa
input()
# se despide
print("Adios")
