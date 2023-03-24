string = "The quick brown fox jumps over the lazy dog"
print(string[20:25])


print(f"combined: {string[4:9]} {string[16:19]}")

print(string.upper())

fname = input("Enter your first name:")
lname = input("Enter your last name:")
age = int(input("Enter your age:"))

print(f"Good Morning, {fname} {lname}, {age} yrs.")
initials = f"{fname[0].upper()}.{lname[0].upper()}"
print("Capitalized Initials: " + initials)
