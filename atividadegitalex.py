import json
from json import JSONEncoder


class Curso:
    def _init_(self, codigo, nome, professor, aluno):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor
        self.aluno = aluno


class Aluno:
    def _init_(self, rm, nome):
        self.rm = rm
        self.nome = nome


# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o._dict_


aluno = Aluno(30985, "Alex")
curso = Curso(1, "Computacao na Nuvem", "Fillipe", aluno)


print("Printing to check how it will look like")
print(EmployeeEncoder().encode(curso))