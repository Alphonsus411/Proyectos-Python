import re

print(re.search(r".com", "welcome"))

print(re.search(r"\.com", "welcome"))  # añadimos el carácter de escape "\" , cambiando el resultado de la búsqueda a negativo,
# porque no hay ningún punto en la palabra o cadena

print(re.search(r"\.com", "mydomain.com"))  # en este caso, el patrón de búsqueda debería coincidir perfectamente

print(re.search(r"\w*", "This is an example"))  # búsqueda de cualquier patrón alfanumérico

print(re.search(r"\w*", "And_this_is_another"))








