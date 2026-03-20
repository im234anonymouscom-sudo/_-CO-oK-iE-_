# Game of Guessing (02/3/2026)


import random
secret=random.randint(1,5)
count=0 
truth=False
while count<=5:
    guess=int(input("number from 1to5"))
    count=count+1
    if guess==secret:
        truth=True
        break
    else:
        print("try")
if truth:
    print(f"you got the correct answer which is {secret} and the attempts taken by you is {count}")
else:
    print(f" dont worry but the secret was {secret}(:")