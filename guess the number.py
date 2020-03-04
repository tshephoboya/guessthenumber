import random

random_number = random.randrange(1,51)
user_number = 0

def guess_number():
    while (True):
        user_number = input("Guess a number between 1-50: ")
        try:
            user_number = int(user_number)
            break
        except ValueError as e:
            print("Please enter a valid number: ")
        
    
    if user_number >= 1 and user_number <=50:
        if user_number == random_number:
            print("Congrats, You have guess the right number.")
            return
        elif user_number < random_number:
            print("The number is too low, plese try again")
            guess_number()
        else:
            print("The number is too high, please try again")
            guess_number()
    else:
        print("Enter number is correct range")
        guess_number()

    


guess_number()
