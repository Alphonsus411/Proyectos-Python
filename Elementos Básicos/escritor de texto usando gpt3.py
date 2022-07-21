# crea un editor de texto de word usando conexión con gpt3

from gettext import npgettext


def __init__(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    self.write = write
    self.read = read
    self.clear = clear
    self.save = save
    self.load = load
    self.run = run


np = npgettext('', '', 1)


# permite ejecutar el editor de texto
def run(self):
    while True:
        print(self.text_buffer)
        text = input()
        self.write(text)
        if text == 'exit':
            break


# permite escribir en el editor de texto
def write(self, text):
    self.text += text
    self.text_buffer_[0, 60] += text
    self.text_buffer_[0, 60] = self.text_buffer_[0, 60][-60:]
    self.text_buffer = self.text_buffer_[0, 60]
    return self.text_buffer


# permite leer el editor de texto
def read(self):
    return self.text


# permite limpiar el editor de texto
def clear(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# permite guardar el editor de texto en un archivo
def save(self, filename):
    with open(filename, 'w') as f:
        f.write(self.text)
    return self.text


# permite cargar un archivo en el editor de texto
def load(self, filename):
    with open(filename, 'r') as f:
        self.text = f.read()
    return self.text


# permite crear un editor de texto
def create(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# permite eliminar un editor de texto
def delete(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# permite editar el editor de texto
def edit(self, text):
    self.text = text
    self.text_buffer = text
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# permite copiar el editor de texto
def copy(self):
    return self.text


# permite pegar el editor de texto
def paste(self, text):
    self.text += text
    self.text_buffer_[0, 60] += text
    self.text_buffer_[0, 60] = self.text_buffer_[0, 60][-60:]
    self.text_buffer = self.text_buffer_[0, 60]
    return self.text_buffer


# permite cortar el editor de texto
def cut(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# cierra el editor de texto
def close(self):
    self.text = ''
    self.text_buffer = ''
    self.text_buffer_ = np.zeros((1, 60))
    return self.text_buffer


# cierra el programa
def exit(self):
    print('exit')
    return self.text


# se despide del programa
def bye(self):
    print('bye')
    return self.text
