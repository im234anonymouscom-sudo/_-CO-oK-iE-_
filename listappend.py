


# umm List.append(new) (9/03/2026))


newlist=[]
user=(input("add items or type DONE to stop")) 
count=0
while user.upper()!= "DONE" :
    newlist.append(user)
    print(f" the list is {newlist} ")
    count= count+1
    user=(input("change"))
print(f" the new list is {newlist} and the number of items is {count} , and {sorted(newlist)}")
 
   
     
    # learning data cleaning  
user = input("give a word").lower().capitalize().strip()
print(user)
