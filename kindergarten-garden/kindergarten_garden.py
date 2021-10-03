dic_planta = {
    "V": "Violets",
    "C": "Clover",
    "R": "Radishes",
    "G": "Grass"
    }
dic_alumnos = {
    "Alice": 0,
    "Bob": 2,
    "Charlie": 4,
    "David": 6,
    "Eve": 8,
    "Fred": 10,
    "Ginny": 12,
    "Harriet": 14,
    "Ileana": 16,
    "Joseph": 18,
    "Kincaid": 20,
    "Larry": 22
    }


class Garden:

    def __init__(self, diagram = '', students = ''):
        if(students != ''):
            self.students = sorted(students)
        else:
            self.students = ''
        self.diagram = diagram.split('\n')
        print(self.students)
        
    def plants(self, students):
        resultado = []
        numero = 0
        if(self.students != ''):
            for x in range(len(self.students)):
                if(students == self.students[x]):
                    numero = x * 2
        else:
            numero = dic_alumnos[students]
        resultado.append(dic_planta[self.diagram[0][numero]])
        resultado.append(dic_planta[self.diagram[0][numero + 1]])
        resultado.append(dic_planta[self.diagram[1][numero]])
        resultado.append(dic_planta[self.diagram[1][numero + 1]])
        return resultado
    