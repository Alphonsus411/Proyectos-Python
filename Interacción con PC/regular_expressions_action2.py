import re

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"   # incluimos en el patrón de búsqueda cualquier número,
# letra o símbolo con esta expresión, pero aislando la búsqueda del salto a otra variable

print(re.search(pattern, "_this_is_a_valid_variable_name"))

print(re.search(pattern, "this isn´t a valid variable"))

print(re.search(pattern, "my_variable1"))

print(re.search(pattern, "2my_variable1"))












