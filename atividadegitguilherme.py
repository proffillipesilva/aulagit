import json
from json import JSONEncoder

class Curso:
    def __init__(self, codigo, nome , professor, aluno):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor
        self.aluno = aluno


        
class Aluno:
    def __init__(self, rm , nome):
        self.rm = rm
        self.nome= nome
        





# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


aluno= Aluno("30999", "Guilherme")
curso = Curso(9000, "TI",  "Fillipe", aluno)


print("Printing to check how it will look like")
print(EmployeeEncoder().encode(curso))
