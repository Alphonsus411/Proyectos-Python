
import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))  # con findall, realizamos una búsqueda completa de coincidencias en toda la cadena de palabras

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))  # con el patrón \b, buscamos las coincidencias en cada palabra

print(re.findall(r"\w{5,10}", "I really like strawberries"))  # con este otro patrón, introducimos búsquedas de cinco y diez letras

print(re.findall(r"\w{5,}", "I really like strawberries"))  # el mismo patrón anterior, pero sin limitaciones

print(re.search(r"s\w{,20}", "I really like strawberries"))  # patrón de búsqueda con hasta 20 caracteres alfanuméricos













