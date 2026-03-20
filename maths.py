
## Matha wave

for i in range(2,50):
    print("*" * i )
for i in range(50,1,-1):
    print("*"* i)
    
## Averages with Lists      
      
markslist=[]    
for i in range(5):
    user=int(input("enter the marks"))
    markslist.append(user)
print(f' the list is {sorted(markslist)} ')
mi=sum(markslist) /len(markslist)
print(f" the average is {mi}")

