import csv # importamos el módulo csv
f = open("data.csv") #invocamos la lectura del archivo
csv_f = csv.reader(f)
for row in csv_f: # creamos una iteración para imprimirlo en pantalla
    country, age, salary, purchase = row
    print("Country: {}, Age: {}, Salary: ¨{}, Purchase: {}". format(country, age, salary, purchase))
