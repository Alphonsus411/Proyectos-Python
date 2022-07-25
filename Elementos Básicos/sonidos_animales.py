class Animal:
    sound = ""


def __init__(self, name):
    self.name = name


def speak(self):
    print("{sound} I´m {name}! {sound}".format(name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink!"


def speak(self):
    pass


class Cow(Animal):
    sound = "Mooo!"

    def speak(self):
        pass


milky = Cow()
milky.speak()

print(milky.speak())
