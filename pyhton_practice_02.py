# Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute
# the apples. These “n” number of apples is provided to harry by his friends, and he can request for few
# more or few less apples.
# You need to print whether a number is in range mn to mx, is a divisor of “n” or not.
#
# Input:
#
# Take input n, mn, and mx from the user.
# -------------------------------------------------------------------------------------------------------------------------
try:
    n = int(input("Enter the number of apple harry have : "))
    mn= int(input("Enter the minimum number : "))
    mx = int(input("What is the maximum number : "))
except ValueError:
    print("Enter integer only! ")
    exit()

for i in range(mn,mx+1):
    if mn == mx:
        print("this is not a range")
        if n%mx==0:
            print(f"The number {mx} is a divisor of {n} ")
            exit()
        if n%mx!=0:
            print(f"The number {mx} is a not divisor of {n} ")
            exit()

    if n%i == 0 :
        print(f"{i} is a divisor of {n}")
    if n%i!=0:
        print(f"{i} is not a divisor of {n}")