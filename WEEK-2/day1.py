import array as arr
str = "hello"
print("ez" in str)  # conditional operator
print(10 != 50)

searchQuote = "I like to play"
check = "P"
if check in searchQuote:
    print(f"{check} is inside of the string: {searchQuote}")
else:
    print(f"{check} is not inside of the string: {searchQuote}")
# not in

name = "Bob Johnson"
vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    if vowel in name:
        print(f"the vowel {vowel} is inside of {name}.")

myArray = arr.array("i", [25, 20, 30, 35, 40, 45])
myList = ["string", "this is text", 21, 25, True]
print(myList)
myTuple = ("string", "this is text", 21, 25, True)
print(len(myTuple))
print(myList)

myWords = ["Rally", "Sights", "Zel", "Grapes", "Apes", "Lots"]
myWords.sort(reverse=True)
print(myWords)
