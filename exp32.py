import re
s = input("Enter a string: ")
pattern = r'^([a-zA-Z]).*\1$'
if re.search(pattern, s):
    print("The given string starts and ends with the same character")
else:
    print("The given string does NOT start and end with the same character")
