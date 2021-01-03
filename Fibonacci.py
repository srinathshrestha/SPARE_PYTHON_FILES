a = 0
b = 1
n = int(input("Enter how many element you want in the series "))
print(a,b, end=" ")
while n-2:
    c = a+b
    a=b
    b=c
    print(c,end=" ")
    n-=1