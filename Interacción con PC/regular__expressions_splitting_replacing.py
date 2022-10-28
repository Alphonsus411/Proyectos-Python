import re

print(re.split(r"[.?!]", "One sentence.Another one? And the last one!"))  # el método split nos permite escaparnos de los caracteres
# reflejados entre los corchetes de la búsqueda, ignorándolos

print(re.split(r"([.?!])", "One sentence.Another one? And the last one!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@myexample.com"))  # el método sub sustituye unas cadenas por otras

print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

















