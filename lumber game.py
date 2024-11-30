import random#importing module
playing = True#initilise
number = str(random.randint(10,20)) # random built-in function
print("i will generate a number from 10 to 20,and you have to guess the number one digit at a time.")
print("the game ends when you get 1 hero")
while playing:
    guess = input("give me youre best guess! \n")
    if number == guess:
       print("you win the game")
       print("the number was", number)
       break

    else:
     print("youre guess isnt quite right try again. \n")