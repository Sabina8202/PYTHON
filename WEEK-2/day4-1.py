"""
to do exception handling we use:
try:

except:


attempt our potentially error-riden code with try statement
python wont crash and return the exception

"""

print("hello world")
try:

    y = 0
    x = 10
    print(x/y)
except ValueError as err:
    print("exception was raised")
print("heres the half of the code")
