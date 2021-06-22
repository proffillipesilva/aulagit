import json
from json import JSONEncoder


class Aluno:
    def __init__(self, rm, name):
        self.rm = rm
        self.name = name


class Curso:
    def __init__(self, Codigo, nome, professor):
        self.codigo = Codigo
        self.nome = nome
        self.professor = professor


# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


Curso = Curso("01", "Jean", "Felipe")
Aluno = Aluno(31003, "Jean Santos")


print("Printing to check how it will look like")
print(EmployeeEncoder().encode(Aluno))
print(EmployeeEncoder().encode(Curso))
