import sys

#com o float passamos um argumento em params para que seja convertido para numero
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number * second_number
result_quotient = first_number / second_number

print(f"{first_number} plus {second_number} equals {result_sum}")
print(f"{first_number} minus {second_number} equals {result_sum}")
print(f"{first_number} multiplied {second_number} equals {result_sum}")
print(f"{first_number} divided {second_number} equals {result_sum}")