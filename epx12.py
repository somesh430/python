s=input("enter a string:")
str_split=s.split(' ')
str_join='_'.join(str_split)
str_dec={idx:ele for idx,ele in enumerate(str_split)}
print("dictionary after splitting:")
print(str_dec)
print("string after join with'_'")
print(str_join)
        
