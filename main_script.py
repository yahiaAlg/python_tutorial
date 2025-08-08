print("----------------------calculator program--------------------")

variable1 = input("give me the first number")
variable2 = input("give me the second number")
print(type(variable1))
print(type(variable2))
variable1 = int(variable1)
variable2 = int(variable2)
eucli_div = variable1 // variable2
div = variable1 / variable2
prod = variable1 * variable2
summation = variable1 + variable2
substraction = variable1 - variable2
exponential = variable1 ** variable2
rest = variable1 % variable2

print("the sum of the two numbers is: ", summation)
print("the product of the two numbers is: ", prod)
print("the division of the two numbers is: ", eucli_div, type(eucli_div))
print("the division of the two numbers is: ", div, type(div))
print("the substraction of the two numbers is: ", substraction)
print("the exponential of the two numbers is: ", exponential)
print("the rest of the two numbers is: ", str(rest))
