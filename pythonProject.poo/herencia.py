# herencia

class Pokemon:
    pass

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        assert isinstance(tipo, object)
        self.tipo = tipo

    def descripcion(self):
        return "{} es un Pokemon de tipo : {}".format(self.nombre, self.tipo)


class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)


class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipo_ataque)


nuevo_pokemon = Pikachu("Richard", "eléctrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto Trueno"))





