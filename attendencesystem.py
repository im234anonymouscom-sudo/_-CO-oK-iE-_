def system():
    
    absentees=[]
    for i in range(1,11):        
         Ans=input(f"Is {i} absent?")
         if Ans.lower().strip()=='yes':        	   
               absentees.append(i)     		    
         else :
   	         print(f" since {i} is present " )                     
    print(f" The total no. of student  absent is {len(absentees)} and the absentees : {absentees} ")
system()