# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
#
# 676, 616, mom, 100001.
#
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number.
# t input should be the number of test cases and then take all the cases as input from the user.
# -------------------------------------------------------------------------------------------------------------------
def next_pal(n):
    n=n+1
    while not palindrome(n):
        n=n+1
    return n
def palindrome(n):
    if str(n)==str(n)[::-1]:
        return f"{n} is palindrome number"



if __name__ == '__main__':
    n = int(input("How many numbers to test : "))
    numbers =[]
    for i in range(n):
        num = int(input("Enter the numbers : "))
        numbers.append(num)

    for i in range(n):
        print(palindrome(numbers[i]))
        print(f'Next palindrome  number for {numbers[i]} is {next_pal(numbers[i])}')
        # if str(n)==str(n)[::-1]:
        #     print(f'{numbers[i]} is a palindrome number.')

