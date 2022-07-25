file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} files with the extension {}".format(amount, ext))

file_counts.keys()  # devuelve una lista con las extensiones de los archivos

file_counts.values()  # devuelve una lista con los valores de las extensiones

for value in file_counts.values():  # recorre los valores de las extensiones
    print(value)
