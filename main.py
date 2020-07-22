# FUNCTIONS - a block instructions to do an action. They're used to organize code.

# 2 things required to do:
# 1) define the function
# 2) call the function

#define a function
#def greeting():
#  print("Hello")

#call function
#greeting()

# function with parameter, a parameter is a value to plug into a function, for the function to use creating an output
#def greeting(name):
#  print("Hello " + name)

#guestname = input("what is your name: ")

#greeting(guestname)

def addNumbers(num1, num2):
  print(num1 + num2)

def subNumbers(num1, num2):
  print(num1 - num2)

# Ask user to enter two numbers. Plug these two numbers into addNumbers function

#addNumbers(2,3)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("add or subtract: ")

if operator.lower() == "add":
  addNumbers(num1, num2)
elif operator.lower() == "subtract":
  subNumbers(num1, num2)
else:
  print("that's not an operator")


