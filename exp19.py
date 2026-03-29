def root(x,n=2):
    return x**(1/n)
x=int(input("Enter a number:"))
n=int(input("Enter a number:"))
res1=root(x,n)
res2=root(x)
print("The value without default n=",res1)
print("The value with default n=",res2)
