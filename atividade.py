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


class Aluno(JSONEnconder):
    def default(self, o):
        return o.__dict__



aluno = Aluno(30987, "Andrew")
curso = Curso(1, "Filipão", "GIT")




print("Teste abaixo")
print(AlunoEnconder().encode(aluno))
