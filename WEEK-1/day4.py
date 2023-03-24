"""def greetings():
    print("hello")
    print("Bom dia")


greetings()


def greeting2(name):
    print("Take care", name)


greeting2("sabina")


def func():
    return "hello"


print(func())


def squareNumber(x):
    return x * x


print(squareNumber(5))"""

# exercise
# Write a function that will Cube a Number.
# Take a single parameter and return the cube (x^3)
"""

from time import sleep
from random import randint, random
from math import sqrt


def cube(num):
    return num * num * num


print(cube(5))

# - Write a function that will add 2 numbers together.
# the function will take 2 parameters and return the sum of them.


def add(num1, num2):
    return num1 + num2


# print("result: " + add(5, 4))
print("result: ", add(5, 4))

# - write a function that will find the average of 3 numbers.
# the function should take 3 parameters and then return the average (sum / 3)


def avg(x, y, z):
    return (x+y+z)/3


print("average: ", avg(5, 4, 9))

# - Write a function that takes a list of numbers, iterates through it and
# finds the total sum of the list.


def tsum(numbers):
    total = 0
    for x in numbers:
        total = total+x
    return total


print(tsum((5, 4, 9)))

myList = [15, 15, 23, 2, 0]


def totalSum(List):
    total = 0
    for num in List:
        total = total + num
    return total


print(totalSum(myList))


print("hi there!")
sleep(3)
print("Trust that beautiful things arre coming your way")
print("Trust the universe")

print(sqrt(49))
"""
