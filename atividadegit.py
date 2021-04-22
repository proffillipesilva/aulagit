import json
from json import JSONEncoder


class Aluno:
    def __init__(self, rm, nome):
        self.rm = rm
        self.nome = nome


class Curso:
    def __init__(self, codigo, nome, professor):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor


# subclass JSONEncoder
class AlunoEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


curso = Curso("codigo", "Informatica", "Fillipe")
aluno = Aluno(31016, "Otavio da Silva Rovere")


print("Printing to check how it will look like")
print(AlunoEncoder().encode(aluno))