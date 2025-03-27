import random
target_number=random.randint(1,100)
#attempts=0
def guess():
    attempts = 0
    print("Welcome to Number Guessing Game")
    print("I am thinking of a number between 1 to 100")
    while True:
        try:
            num=int(input('Enter your Guess'))
            attempts+=1
            if num<1 or num>100:
                print("Please enter a number between 1 to 100")
                continue
            if num>target_number:
                print("the NUmber is too Higher Number")
            elif num<target_number:
                print("Too high! try a lower number")
            else:
                print(f'Congratulations! you ve guessed the number{target_number}')
                print(f'It took {attempts} attempts')
                break
        except:
            print("please enter a valid number")
play_again=input("Do you want to play agian (y|n)").lower()
if play_again == "y":
    guess()
else:
    print("thanks for playing goodbye")

