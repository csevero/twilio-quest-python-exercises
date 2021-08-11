import sys

#pegando toda a lista do argv
numbers = sys.argv

#o .pop irá remover o index que for passado via params do array, nesse caso o index 0 é o nome do arquivo que não é útil para nós
numbers.pop(0)

#dando um for na nossa lista, criando uma var number e fazendo as verificações
for item in numbers:
  number = int(item)
  if(number % 3 == 0 and number % 5 == 0):
    print('fizzbuzz')
  elif(number % 3 == 0):
    print('fizz')
  elif(number % 5 == 0):
    print('buzz')
  else:
    print(number)