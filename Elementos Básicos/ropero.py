# first want to iterate through the elements of the dictionary and then through the elements
# of the list.
wardrobe = {'shirt': ['red', 'blue', 'white'], "jeans": ['blue', 'black']}
for key, value in wardrobe.items():
    print(key)
    for item in value:
        print("{}={}".format(key, item))
