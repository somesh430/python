string1=input("Enter string1:")
string2=input("Enter string2:")
if len(string1)==len(string2):
    print("strings with same length")
    for i in range(len(string1)):
                   print(string1[i],end="")
                   print(string2[i],end="")
else:
    print("Strings with different length")
