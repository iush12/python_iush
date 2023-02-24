# guess the number game : between 100 numbers

import random
a=random.randint(0,100)

attemps=0
max_attemps=5


while max_attemps>attemps:
    guess=int(input("enter a number:"))

    attemps+=1
    if(guess==a):
        print("you are correct")

    elif(guess>a):
        print("guess lower ")

    else:
        print("think higher")
if(attemps==max_attemps):
    print("nice try the answer was",a)        
