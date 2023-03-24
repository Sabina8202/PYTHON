from math import sqrt
from random import randint

result = int(input("enter any number: "))
print(sqrt(result))

# import random randint(x, y) let the user input 2 numbers,
# generate a number between the range of those 2 numbers
# given.
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number:"))
result1 = randint(num1, num2)
print("random number: ", result1)

# Take a name from the user and generate a random number:
# make a concatentating their name and a
# random generated number.

name = input("Enter any string: ")
num = str(randint(0, 100))
print("My name is " + name + "." + " I am " + num + " years old.")
