person = {
    "firstName": "Bob",
    "LastName": "Johnson",
    "age": 25,
    "bio": "A straight forward man"

}
# how to access from dictionary

print(person["firstName"])
person.update({"age": 26})
print(person)

# adding/removing values
person.pop("bio")
print(person)

person.update({"job": "Engineer"})
del person["age"]
print(person)

mySet = {"a", "a", "b", "z", "x", 101, 15, 25, 35}
# accessing

findItem = "h"
if findItem in mySet:
    print("This is true")
else:
    print("This is false")
mySet.pop()
print(mySet)

"""
squareList = []
for i in range(1, 10):

    squareList.append(i*i)
    print(squareList)"""

x = 10
squareNum = [(i**2) for i in range(x)]
print(squareNum)
print("\nfinding common numbers:")
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [10, 11, 12, 5, 6, 7, 16]
commonAB = [a for a in listA if a in listB]
print(commonAB)

listC = [(a, "Apples") for a in listA]
print(listC)

listD = [("Apple", "Banana", "Canberry") for i in range(20)]
print(listD)


# 2D-List
list2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list2D[1][1])
list2D[1][1] = 60
print(list2D)
