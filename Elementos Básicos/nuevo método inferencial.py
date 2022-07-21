# NMI significa exposición ordenada de una premisa, razonamiento deductivo basado en el sentido común y en los datos disponibles,
# que o bien pueden ser procedentes de un estudio sociológico o pruebas de laboratorio, 
# pero no toma decisiones finales hasta haber completado perfectamente los pasos para llegar a juzgar algo como "útil", como "verdadero", o como "falso". 
# Cualquier premisa es verdadera cuando se ha demostrado su fiabilidad y su realidad, esto es, cuando hay pruebas fehacientes de su veracidad. Si no, no es que no sea verdadera, sino sigue siendo una hipótesis o una teoría o razonamiento deductivo, pero no una afirmación de realidad palpable y cognitiva. 
# Cualquier premisa es falsa cuando se ha demostrado su poca o escasa fiabilidad y completa irrealidad, cuando tenemos pruebas de su falsedad. Si no, ocurre como en la anterior premisa, se queda como un razonamiento deductivo o hipótesis, pero no es una negación en sí misma. 
# Para una demostración válida, se han de presentar pruebas sólidas de la misma, bien razonada, expuesta, con los resultados y datos analíticos o de laboratorio fehacientes y aportados por profesionales del sector o tema a tratar, siempre asegurándose varias veces de que no ha habido contaminación conceptual y la imparcialidad es total. Si la exposición no está bien razonada, no debe ser aceptada bajo ningún concepto, so riesgo de caer en un procedimiento cerrado de falsedad. 
# Las demostraciones deben estar perfectamente acotadas, esto es, deben centrarse en el tema o disciplina o pregunta planteada y no perderse por caminos diferentes, porque se debe trabajar el tema en concreto, no derivaciones o deducciones de éste. Se debe buscar una respuesta a una pregunta planteada. 
# Las premisas siempre han de ser tratadas como deducciones lógicas, no como leyes o postulados incluso antes de ser razonadas o expuestas, investigadas o comprobadas mediante los instrumentos analíticos y los medios logísticos o disciplinas adecuadas (estadística, laboratorio experimental, método científico, etc.). Una premisa es simplemente un procedimiento deductivo, no una afirmación verdadera o falsa. No confundamos nunca los términos, en los que muchos filósofos e intelectuales han cometido un craso error, al considerar todo su pensamiento dogma y todas sus deducciones una especie de "doctrina mística" a seguir, eso corre el peligro de contaminación conceptual o de anteponer las opiniones propias a las de un grupo de pensadores serios o una comisión de trabajo preparada perfectamente para resolver la investigación. 
# Deben abordarse siempre temas desde un punto de vista de la utilidad práctica o social, esto es, no hay que responder a todas las preguntas que se planteen por método inferencial o deductivo, abandonando los temas inválidos para cubrir las necesidades del colectivo para el que se trabaje. Si algo no es útil, se deja para cuando realmente lo sea o se necesite abordar desde otros puntos de vista.  
# La decisión final sobre la veracidad o falsedad de la investigación de cualquier naturaleza, debe estar adecuada al consenso de varios profesionales de una disciplina o especialidad, nunca jamás a los caprichos personales de un solo orador que habla consigo mismo en sus escritos y jamás cuenta con las opiniones ajenas. Hay muchos intelectuales que hablan con la pared, y como esta no les replica, pues se dan por contentos y producen toneladas de "papel mojado" que no sirve para nada. Eso no es útil, pierde su veracidad y su objetividad. 
# Si una premisa o postulado queda incompleto, pues no puede terminarse su razonamiento, al no disponerse de las herramientas, las experiencias personales o los datos estadísticos necesarios para llegar a una conclusión válida. No debe ser desechada, sino pospuesta según el procedimiento citado anteriormente. 
# La verdad de una premisa, o su mentira, queda determinada por su utilidad, por su veracidad comprobada y por su credibilidad, siempre que haya quedado bien explicada, razonada o argumentada, y previamente demostrada. 
# El razonamiento o deducción de una premisa es verdadero cuando se apoya en pruebas válidas y herramientas de investigación adecuadas (laboratorios, estadísticas, encuestas no falseadas, datos informáticos o matemáticos, etc.), en un erudito que sea competente en la materia de la que habla, y que no contamine el mismo con sus opiniones personales, sea imparcial y haga un trabajo inferencial apropiado e independiente. 
# Una deducción o inferencia, tiene que pasar por el razonamiento adecuado para llegar a buen puerto, y apoyarse en pruebas sólidas, sino, pasa a ser una hipótesis, pero no puede decidirse todavía si es verdadera o falsa (ya que su veracidad y credibilidad no han sido del todo comprobadas). El no llegar a una conclusión válida sobre un tema, no demuestra que éste sea una falsedad, sino que no puede colegiarse o llegarse a buen puerto con las herramientas disponibles, por lo cual, debe investigarse otro asunto o dejarse para después. 
# Un razonamiento es adecuado o verdadero cuando el que lo expone está acreditado o documentado suficientemente en una materia, área de conocimiento o especialidad, tiene una carrera profesional contrastada y una credibilidad auténtica, independientemente de lo bien que hablen los demás de ese "sabio" (porque en España hay muchos sabios de taberna, y muchos adictos al púlpito, pero ninguno está verdaderamente entre los que realmente deberían trabajar por la comunidad civil y su bienestar). 
# Una investigación debe basarse en un tema en concreto, no perderse en temas derivados, divagaciones escolásticas o deducciones incorrectas, o catalogaciones y opiniones personales, estamos tratando con una inferencia o deducción lógica, no con un tratado sobre la moralidad o las tendencias políticas de un "erudito polarizado". Cualquier contaminación ideológica o de opinión, invalida completamente la investigación, por concienzuda y profesional que haya sido ésta. La tesis o hipótesis seguiría en su estado de proposición, y no de inferencia deductiva. 

# Creamos la clase del NMI:
class NMI:
    premisa = ""
    conclusion = ""

    def __init__(self, premisa, conclusion):
        self.premisa = premisa
        self.conclusion = conclusion

    def __str__(self):
        return "NMI: " + self.premisa + " -> " + self.conclusion

    def __repr__(self):
        return "NMI: " + self.premisa + " -> " + self.conclusion

    def __eq__(self, other):
        return self.premisa == other.premisa and self.conclusion == other.conclusion

    def __hash__(self):
        return hash(self.premisa + self.conclusion)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.premisa < other.premisa and self.conclusion < other.conclusion

    def __gt__(self, other):
        return self.premisa > other.premisa and self.conclusion > other.conclusion

    def __le__(self, other):
        return self.premisa <= other.premisa and self.conclusion <= other.conclusion

    def __ge__(self, other):
        return self.premisa >= other.premisa and self.conclusion >= other.conclusion

    def __cmp__(self, other):
        if self.__eq__(other):
            return 0
        elif self.__lt__(other):
            return -1
        else:
            return 1


# Creamos la clase de la base de datos:
class BaseDeDatos:
    def __init__(self):
        self.base = []

    def __str__(self):
        return str(self.base)

    def __repr__(self):
        return str(self.base)

    def __len__(self):
        return len(self.base)

    def __getitem__(self, key):
        return self.base[key]

    def __setitem__(self, key, value):
        self.base[key] = value

    def __delitem__(self, key):
        del self.base[key]

    def __contains__(self, item):
        return item in self.base

    def __iter__(self):
        return iter(self.base)

    def __next__(self):
        return next(self.base)

    def append(self, item):
        self.base.append(item)

    def extend(self, item):
        self.base.extend(item)

    def remove(self, item):
        self.base.remove(item)

    def clear(self):
        self.base.clear()

    def index(self, item):
        return self.base.index(item)

    def count(self, item):
        return self.base.count(item)

    def sort(self, *args, **kwargs):
        self.base.sort(*args, **kwargs)

    def reverse(self):
        self.base.reverse()

    def copy(self):
        return self.base.copy()

    def pop(self, index):
        return self.base.pop(index)

    def popitem(self):
        return self.base.popitem()

    def extend(self, item):
        self.base.extend(item)

    def insert(self, index, item):
        self.base.insert(index, item)

    def sort(self, *args, **kwargs):
        self.base.sort(*args, **kwargs)

    def reverse(self):
        self.base.reverse()

    def copy(self):
        return self.base.copy()

    def count(self, item):
        return self.base.count(item)

    def index(self, item):
        return self.base.index(item)

    def remove(self, item):
        self.base.remove(item)

    def clear(self):
        self.base.clear()

    def copy(self):
        return self.base.copy()


# Creamos la clase de la base de datos de NMI:
class BaseDeDatosNMI(BaseDeDatos):
    def __init__(self):
        BaseDeDatos.__init__(self)

    def __str__(self):
        return str(self.base)

    def __repr__(self):
        return str(self.base)

    def __len__(self):
        return len(self.base)

    def __getitem__(self, key):
        return self.base[key]

    def __setitem__(self, key, value):
        self.base[key] = value

    def __delitem__(self, key):
        del self.base[key]

    def __contains__(self, item):
        return item in self.base

    def __iter__(self):
        return iter(self.base)

    def __next__(self):
        return next(self.base)

    def append(self, item):
        self.base.append(item)

    def extend(self, item):
        self.base.extend(item)

    def remove(self, item):
        self.base.remove(item)

    def clear(self):
        self.base.clear()

    def index(self, item):
        return self.base.index(item)

    def count(self, item):
        return self.base.count(item)

    def sort(self, *args, **kwargs):
        self.base.sort(*args, **kwargs)

    def reverse(self):
        self.base.reverse()

    def copy(self):
        return self.base.copy()

    def pop(self, index):
        return self.base.pop(index)

    def popitem(self):
        return self.base.popitem()

    def extend(self, item):
        self.base.extend(item)

    def insert(self, index, item):
        self.base.insert(index, item)


# ahora definimos la aplicacion del metodo inferencial:
def aplicar_inferencial(base_de_datos, base_de_datos_nmi):
    # creamos una lista con hasta 3 elementos:
    lista_de_nmi = []
    # recorremos la base de datos:
    for premisa in base_de_datos:
        # recorremos la base de datos de NMI:
        for nmi in base_de_datos_nmi:
            # si la premisa de la base de datos es igual a la premisa de la base de datos de NMI:
            if premisa == nmi.premisa:
                # añadimos el NMI a la lista:
                lista_de_nmi.append(nmi)
    # devolvemos la lista de NMI:
    return lista_de_nmi


# definimos premisa y conclusion:
premisa = Premisa('p', 'q')
conclusion = Premisa('q', 'r')


# definimos Premisa
class Premisa:


# despues aplicamos el metodo de inferencial a la base de datos de NMI:
base_de_datos_nmi = BaseDeDatosNMI()
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q1'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q2'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q3'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q4'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q5'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q6'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q7'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q8'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q9'))
base_de_datos_nmi.append(NMI(premisa('p1', 'p2', 'p3'), 'q10'))
