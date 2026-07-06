def givetheAP(x, y, z):
    mylist = []
    for n in range(x, y + 1):
        if n % z == 0:
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