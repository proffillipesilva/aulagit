import json
from json import JSONEncoder


class Aluno:
    def __init__(self, RM, NAME):
        self.RM = RM
        self.NAME = NAME


class Curso:
    def __init__(self, COD, NOME, PROF):
        self.COD = COD
        self.NOME = NOME
        self.PROF = PROF


# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

Aluno = Aluno(31008, "Leo Maffeis")
Curso = Curso(01, "LEO", "Felipe")



print("Printing to check how it will look like")

print("-" * 50)

print(EmployeeEncoder().encode(Curso))
print(EmployeeEncoder().encode(Aluno))

