# Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b
# are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and
# your program must tell whether the number is greater than the actual number or less than the actual number. Log the
# number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum
# number of trials wins! Randomly generate a number after taking a and b as input and don’t show that
# to the user.
# ----------------------------------------------------code area---------------------------------------------------------

import random
def guss(a,b,real_num):
    n = int(input(f"Enter your guss between {a} & {b}: "))
    chance = 1
    while n!= real_num:
        if n < real_num :
            n = int(input("Enter a bigger number : "))
            chance = chance+1
        else:
            n = int(input("Enter a smaller number : "))
            chance = chance+1
    print(f"CORRECT!! You have gussed the number in {chance} attempt. ")
    return chance



if __name__ == '__main__':
    a = int(input("Enter the 1st number : "))
    b = int(input("Enter the 2nd number : "))

    print("PLAYER 1 turn >>")
    real_num_1 = random.randint(a, b)
    first_try= guss(a,b,real_num_1)

    print("PLAYER 2 turn >>")
    real_num_2 = random.randint(a, b)
    Second_try= guss(a,b,real_num_2)

    #----------------------------------------
    if first_try > Second_try :
        print(f"The actual number was {real_num_1} which is  answerd by PLAYER 1 in {first_try} attempts")
    elif Second_try>first_try:
        print(f"The actual number was {real_num_2} which is answerd by PLAYER 2 in {Second_try} attmepts")
    else:
        print("Its a tie!!")
