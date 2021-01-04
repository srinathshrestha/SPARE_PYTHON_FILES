def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


# print(factorial(int(input("Enter the number :\n"))))


# -------------------------------------------------------------4

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
x = fact(int(input("Enter the number :")))
print(f'factorial is {x}')