import csv

users = [{'name': 'Sol Mansi', "username": "solm", "deparment": "IT infraestructure"} ,  # creamos unas listas de usuarios con sus claves y parámetros a modo de diccionarios
         {"name": "Lio Nelson", "username": "lion", "deparment": "User Experience Research"},
         {"name": "Charilie Grey", "username": "greyc", "deparment": "Development"}]

keys = ["name", "username", "deparment"] # fijamos las palabras clave
with open('by_deparment.csv', 'w') as by_deparment:
    writer = csv.DictWriter(by_deparment, fieldnames=keys) # método de creación y separación de diccionarios en archivos csv
    writer .writeheader() # llamamos a la ordenación por encabezamiento
    writer.writerows(users) # llamamos a las columnas por usuario
    
with open('by_deparment.csv', 'r') as by_deparment:
    reader = csv.DictReader(by_deparment)
    for row in reader:
        print(row)  

# Path: Interacción con PC\CSV_dictionaries.py








