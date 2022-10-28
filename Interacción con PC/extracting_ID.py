import re

log = "July 31 07:51:48  mycomputer bad_process[12345]: ERROR Performing Package Upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])


def extract_pid(log_line):
    regex = r"\[(\d+)\]"  # patrón para búsqueda numérica entre corchetes
    result = re.search(regex, log_line)
    if result is None:
        return ""  # si no se cumple la condición, devolvemos un resultado vacío
    return result[1]


print(extract_pid(log))  # llamamos a la búsqueda para la línea de registro del
# primer ejemplo para comprobar el funcionamiento de nuestra función

print(extract_pid("99 elephants in a [cage]"))







