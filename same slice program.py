import math

pizzaslices = 8
family = 4

eat =int(input("number of slices eaten by each person"))

totalslices = eat*family

print("number of total slices eaten", totalslices)

wholepizza = math.ceil(totalslices/pizzaslices)

print("whole pizzas to order", wholepizza)

leftbymodulo = totalslices%pizzaslices

print ("Leftovers", leftbymodulo)
