"""
Author: RL
Date: 2023-02-22
Time: 30 Minutes

Read the Questions and Answer Them as best as you can.
"???" Fill in the Gaps.

"""

# Excercise 1
"Given TupleA, find the occuraces of 20"
TupleA = (10, 20, 30, 40, 20, 30, 10, 10)
print(TupleA.count(20))

# Excercise 2
"Given the Dictionary: person. Do a.) and b.) below"
person = {
    "firstName": "George",
    "lastName": "Johnson",
    "Age": 24,
    "Bio": "A Laid back person.",
    1: "Some First data",
    2: "Some Secondary Data",
    3: 50000
}

# a.) Delete the Keys 1, 2, 3.
del person["firstName"]
del person["lastName"]
del person["Age"]
# b.) Add an Address to the Person
person.update({"Address": "London"})
print(person)


# Excercise 3
"Given setA, verify that Adam and Amy are inside the set."
setA = {21, 6.9, -6, "Adam", "Danielle", "Pauline", 200, "Amy", "Third"}
if "Amy" and "Adam" in setA:
    print("Yes!")
else:
    print("No!")

# Excercise 4
"Access and Print the values from the 2D list, stated below"
twoList = [
    [12, 43, 7523],
    [2467, 31, 553],
    [53, 32, 43]
]
# Access 12
print(twoList[0][0])
# Access 53
print(twoList[2][0])
# Access 31
print(twoList[1][1])

# Excercise 5
"Use List Comprehension to Generate a sequence of the first 10 Cubed Numbers"
x = 10
list = [(i*i*i) for i in range(10)]
print(list)

# Excercise 6
"Given a List namesA, Use List Comprehension to generate a new list with the Length of Each Word."
namesA = ["Ryan", "Lucy", "Kim", "Xin Zhao", "George", "Jake", "Oliver"]
list1 = [len(namesA[i]) for i in range(len(namesA))]
print(list1)
