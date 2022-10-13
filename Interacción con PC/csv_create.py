# importamos el archivo necesario, csv
import csv
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]] # creamos unas listas de servidores para el archivo
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv) # llamamos a la función escritora
    writer.writerows(hosts) # llamamos a las filas escritas




