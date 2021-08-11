
import sys


# o sys.argv funciona como se fosse o process.argv do JS, onde o [0] é o nome do arquivo e a partir do [1] são os dados passados via linha de comando, precisamos utilizar um f antes da nossa string para que ele entenda que vamos passar uma variável ali dentro, já vemos a diferença de Py para JS também na hora de chamar as variáveis dentro de strings
#https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals o f permite que a gente passe dados dentro da nossa string
print(f"{sys.argv[1]}")
print(f"{sys.argv[2]}")
print(f"{sys.argv[3]}")