def givetheAP(x, y, z):
    mylist = [rem=x%z
    if rem==0:
    	a=x]

    else:
    	a=x+(z-rem)
    rem2=y%z
    if rem2==0:
    	l=y
    else:
    	l=y-rem2    
    for n in range(a,y + 1,z):
        
            mylist.append(n)
    return mylist
user = input("So are you ready?? This will tell you the number that lie between x and y and are divisible by z ")

while True:


    if user.capitalize() == "Yes":
        x = int(input('tell the starting of the range: '))
        y = int(input('tell the ending of the range: '))
        z = int(input('tell the dividend: '))

        result = givetheAP(x, y, z)
        print(f"the numbers that are divisible to {z} between {x} and {y} are {result}")
        break

    else :
        
        user=input("type Yes to continue ")
