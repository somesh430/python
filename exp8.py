vowels="aeiouAEIOU"
word=input("Enter a word:")
flag=0
for char in word:
    if char in vowels:
        flag=1
        break
if flag==1:
     print("given string contains vowels")
else:
     print("given string does not contains vowels")
