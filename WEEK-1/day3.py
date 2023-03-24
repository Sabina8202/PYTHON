"""x = 5
if x < 10:
    print("Correct")
else:
    print("Incorrect")


x = 0
if x > 0:
    print("positive")

elif x == 0:
    print("Zero")

else:
    print("negative")


#1 Create a program that lets a user input their age, checks if they are old enough to vote (over 18)
age = int(input("Enter you age:"))
if age > 18:
    print("You are eligible to vote!")
else:
    print("Sorry, You cannot vote")


#2
# Create a program that lets a user enter 2 numbers. Compare them and print to the user:
#   if the first is greater the other ,
#   if the second is greater then the other
#   or if they are both equal

a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

if a > b:
    print("1st number is greater than 2nd number")

elif a < b:
    print("2nd number is greater than 1st number")

else:
    print("Both are equal")

# 3 Create a program that lets a user enter their score between 0 and 100 and it will grade the score
#   A: 80 - 100
#   B: 60 - 79
#   C: 40 - 59
#   D: 20 - 39
#   E: 0 - 19

score = int(input("Enter your score: "))
if score >= 80 and score <= 100:
    print("Your grade: A")
elif score >= 60 and score <= 79:
    print("Your grade is: B")
elif score >= 40 and score <= 59:
    print("Your grade is: C")
elif score >= 20 and score <= 39:
    print("Your grade is: D")
elif score >= 0 and score <= 19:
    print("Your grade is: E")
else:
    print("Invalid score")


for i in range(1, 10):
    print("helo", i)


fruits = ["orange", "apple", "banana", "lychee"]
for element in fruits:
    print(element)

x = 0
while x <= 10:
    print("hello world", x)
    x = x+1

# Ex 1.) String Repeater: create a program that will repeat print a number of times:
# let the user input both the string and the number of times they'd like to repeat it.

str = input("enter a string: ")
num = int(input("enter a number: "))
for i in range(num):
    print(str)
"""

# Ex 2.) Create a program that will ask the user to guess a passcode.
# # should keep on asking contiously until they get it right.
# # set a passcode variable
# # let the user enter a guess at the passcode
# # check if they got it right or wrong: loop continously until they get it right.

guess = " "
passcode = "abc"

while guess != passcode:
    guess = input("enter the passcode: ")
print("access granted")
