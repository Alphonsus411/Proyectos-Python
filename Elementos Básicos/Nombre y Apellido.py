def nametag(first_name, last_name):
    # Formatea el apellido dando solo la primera letra en mayúscula y un punto
    return ("{} {}.".format(first_name.title(), last_name[0].upper()))


print(nametag("Jane", "Smith"))
# should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# should display "Francesco R."
print(nametag("Jean-Luc", "Danpierre"))
# should display "Jean-Luc D."
