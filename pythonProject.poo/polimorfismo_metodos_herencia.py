# polimorfismo por funcion

class Tomate:
    def tipo(self):
        print("vegetal")

    def color(self):
        print("rojo")


class Manzana:
    def tipo(self):
        print("fruta")

    def color(self):
        print("amarillo")


def funcion(objeto):  # usamos el polimorfismo creando una funcion
    # para un objeto fuera de las clases, pero que
    # presenta los mismos métodos
    objeto.tipo()
    objeto.color()


nuevo_tomate = Tomate()  # creamos un nuevo objeto,
# pero usando los parametros de la funcion con polimorfismo
funcion(nuevo_tomate)

nueva_manzana = Manzana()
funcion(nueva_manzana)




