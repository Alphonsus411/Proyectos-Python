# Remember our Person class from the last video?
# Let’s add a docstring to the greeting method. 
# How about, “Outputs a message with the name of the person.”

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hi, my name is {self.name}"

            
            
Otello = Person("Otello")
print(Otello.greeting())





