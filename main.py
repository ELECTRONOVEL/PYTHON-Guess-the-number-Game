import random

n = random.randint(0,101)


def guess():


    i=0

    while True:
        user = int(input("Enter Your Guess :  "))
        i +=1

        if user == n:

            print(f"Congratulations !!, You have guessed the correct number in {i} attempts")
            return 
        
        elif user>n:
            print("Guess Lower Number !!")
            

        elif user<n:

            print("Guess Higher Number !!")

        

guess()