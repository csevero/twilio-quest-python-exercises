#Criando uma class com nome Citizen, a linha 3 se refere a uma descrição que pode ser dada a classe, fica entre 3 aspas, dentro da classe pode ser definido normalmente variáveis e também métodos
class Citizen():
  """This is my first class in python"""
  greeting = "For the glory of Python!"

  #a classe abaixo com nome __init__ ela sempre será executada assim que a classe for instanciada, ahaha, igual o constructor em javascript, em relação aos params, o self sempre para de uma forma mais rápida definirmos variaveis para nossa classe, então nosso método inicial recebe 2 nomes e usam o self para 'criar' essas variáveis dentro da classe
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  # function que retorna o nome e o sobrenome separado por espaço, aqui vamos que usando o self conseguimos acessar tudo de dentro da classe, parecido com o this do JS, top
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
