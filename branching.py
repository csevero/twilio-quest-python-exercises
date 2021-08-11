import sys

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
result_sum = num1 + num2

#usando if, elif (ou else if em JS) e else
if(result_sum <= 0):
  print('You have chosen the path of destitution.')
elif(result_sum > 1 and result_sum <= 100):
  print('You have chosen the path of plenty.')
else:
  print('You have chosen the path of excess.')