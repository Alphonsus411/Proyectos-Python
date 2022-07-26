# polimorfismo con métodos

class Espana:
    def capital(self):
        print("Madrid")

    def idioma(self):
        print("Espanol")

class Francia:
    def capital(self):
        print("Paris")

    def idioma(self):
        print("Francés")


espanol = Espana() # en el polimorfismo por métodos,
# siempre es aconsejable crear un mínimo de dos objetos para poder
# usar esta propiedad

frances = Francia()

for pais in (espanol, frances):
    pais.capital()
    pais.idioma()





