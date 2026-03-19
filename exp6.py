import random
a=random.randrange(1,10)
b=int(input("Enter a number:"))
while a!=b:
    b=int(input("guess a number between 1 and 10:"))
print("well guessed!")
