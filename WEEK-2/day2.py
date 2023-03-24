"""
Author: RL
Date: 2023-02-20
Time: 30 Minutes

Read the Questions and Answer Them as best as you can.

"""

# Excercise 1
"Given NumListA, Write code that will iterate through the list and find the Total Sum of the list"
numListA = [2, 20, 10, 30, 20, 40, 51, 32, 20]
Sum = 0
for i in numListA:
    Sum = Sum + i
print("Total:", Sum)

# Excercise 2
"This Program will Let the User Build list and print it."
"The program should first ask the user how long they want the list to be, then let them keep on entering values until its full."

# Un-Comment and Complete the program below, filling in the gaps (???)

List2 = []
listLength = int(input("How long do you want the list to be?"))
for index in range(listLength):
    value = input("what would you like to enter")
    List2.insert(index, value)

print(List2)


# Excercise 3
"Given a Value and a quantity, Write Code that will generate a list that repeats the same item, by the quantity Specified"
val = "apple"
quantity = 5
myList = []

for quantity in val:
    myList.append(val)

print(myList)

# Excercise 4
"Given a List of Strings, Write Code that will reverse Each of the strings Inside the list."
List4 = ["Melon", "Banana", "Apple", "Cherry"]
List4a = []
for i in List4:
    List4a.append(i[::-1])

print(List4a)

# Excercise 5
"Given the List of Strings, Complete the code so that the program will Count the number of times a string in the list Starts with a given Prefix."
# Hint: use the startswith() function
List5 = ["car", "dog", "cat", "tree", "cattle", "bush", "camera"]
prefix = "ca"
count = 0
# Complete the Program
for word in List5:
    if word.startswith(prefix):
        count = count + 1

print("number: ", count)
