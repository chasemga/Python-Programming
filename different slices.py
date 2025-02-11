import math

pizzaslices = 8
family = 4

person1 = int(input("how many slices will person 1 eat"))
person2 = int(input("how many slices will person 2 eat"))
person3 = int(input("how many slices will person 3 eat"))
person4 = int(input("how many slices will person 4 eat"))

#eat =int(input("# of slices eaten by each person"))

totalslices = person1 + person2 + person3 + person4

print("number of total slices eaten", totalslices)

wholepizza = math.ceil(totalslices/pizzaslices)

print("whole pizzas to order", wholepizza)

leftbymodulo = totalslices%pizzaslices

print ("Leftovers", leftbymodulo)
