import json
from json import JSONEncoder

class Aluno:
  def __init__(self,rm,nome):
    self.rm = rm
    self.nome = nome

class Curso:
  def __init__(self, codigo, nome, professor):
    self.codigo = codigo
    self.nome = nome
    self.professor = professor

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

aluno = Aluno(1, 'Matheus')
curso = Curso(1, 'Informatica', 'Felipe')

print('Printing to check how it looks like')
print("")
print(EmployeeEncoder().encode(aluno))
print("")
print(EmployeeEncoder().encode(curso))