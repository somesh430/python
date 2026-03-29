import random;
mylist = []
for x in range(20):
    n=random.randint(1,100)
    mylist.append(n)
mylist.sort()
print(mylist)
print('Max=',max(mylist))
print('Min=',min(mylist))
print('second max=',mylist[-2])
print('second min=',mylist[2])
noeven=0
for i in mylist:
    if i%2==0:
        noeven=noeven+1
print('event=',noeven)
