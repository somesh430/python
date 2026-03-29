feet=int(input("Enter length in feet:"))
while True:
    print('\n 1.inches')
    print('2.yard')
    print('3.miles')
    print('4.millimeters')
    print('5.centimeters')
    print('6.meters')
    print('7.kilometers')
    print('8.exit')
    ch=int(input("Enter your choice"))
    if ch==1:
        res=feet*12
    elif ch==2:
        res=feet/3.0
    elif ch==3:
        res=feet*5280.0
    elif ch==4:
        res=feet*304.8
    elif ch==5:
        res=feet*3048
    elif ch==6:
        res=feet*0.3048
    elif ch==7:
        res=feet*0.0003048
    elif ch==8:
        print("exiting program:...")
        break
    else:
        print('invalid choice!try again')
    continue
    print('the request result',res)
