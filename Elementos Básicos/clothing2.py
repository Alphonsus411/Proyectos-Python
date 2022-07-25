# Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission:
# Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. 
# When you’re finished, the script should add up to 10 cotton Polo shirts.

from collections import Counter


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, material, amount):
        Clothing.stock('name').append(self.name)
        Clothing.stock('material').append(material)
        Clothing.stock('amount').append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0

    for item in Clothing.stock('material'):
        if item == material:
            count += Clothing.stock('amount')[n]
        n += 1

    return Counter
