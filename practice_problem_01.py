# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of modules like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sort of errors like:                       (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
# ---------------------------------------------------------------------------------------------------------------------
while True:
    age_yr=int(input("Enter your current age or Year of Birth : "))
    if age_yr > 1900 and age_yr < 1918 :
        print("you seems to be oldest person alive. ")
        exit()
    elif age_yr > 1918 and age_yr< 2021 :
        print(f'you are going to be of 100 on the year {int(age_yr+100)} ')
    elif age_yr< 100 :
        print(f'you are going to be of 100 on the year {2021+(100-age_yr)} ')
    else:
        print(f"{age_yr} is not a VALID input as per the promt.")
        exit()

print("(optinal)")
yr = int(input("Enter the year in which you want know your age : " ))
if yr > 1918 :
  a = yr - 2021
  c = age_yr+a
  print(f'you are going to be of {c} on the year {yr} ')

