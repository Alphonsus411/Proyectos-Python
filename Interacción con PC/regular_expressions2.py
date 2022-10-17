import re # el módulo re se usa para buscar coincidencias en cadenas de palabras
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log) # search es el método usado del módulo re para estas búsquedas
print(result[1])




