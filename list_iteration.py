# groceries = ['apples', 'coffee','pizza rolls','olives']

#for em python
# for item in groceries:
#   string_to_print= f"{item}"
#   print(string_to_print)

#for usando index, precisamo passar o enumerate que recebe a lista no primeiro param e no segundo o número que iniciará que definimos como 1
# for index, item in enumerate(groceries, start=1):
#   string_to_print= f"{index}. {item}"
#   print(string_to_print)

import sys

names = [sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4], sys.argv[5]]

for index, item in enumerate(names, start=1):
  string_to_print = f"{index}. {item}"
  print(string_to_print)