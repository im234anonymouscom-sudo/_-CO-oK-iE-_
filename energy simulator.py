# Energy Simulator (5/03/2026)


sleep=True
Study=True
Energy=int(input("enter your hp"))

while Energy>= 20:
    
    next_day=input('choose maths or science')
    if next_day =="maths" :
         print("study the exercises ")
    elif next_day=="science":
         print("study theories")
    else:
        next_day=input("maths or science")
    sleep=False
    break
    
    
if Energy <20:
    study=False
if sleep==False :
    print(f"go,study ,you have a lot of energy i.e{Energy}")
else:
    print("sleep")