class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.color}"


print("Roses are {}".format(Flower("rose", "red")))
color = 'uknown'

rose = Flower("rose", "red")
rose.color = "red"

violet = Flower("violet", "blue")
violet.color = "blue"

this_pun_is_for_you = True

print("violets are {},".format(violet.color))
print(this_pun_is_for_you)
