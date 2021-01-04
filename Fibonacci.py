# a = 0
# b = 1
# n = int(input("Enter how many element you want in the series "))
# print(a,b, end=" ")
# while n-2:
#     c = a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n-=1

n = int(input('Enter till how many no. you want : '))
a = 0
b = 1
if n==1:
    print(a)

else:
    print(a)
    print(b)
    for i in range(n):

        print(a)
        c = a
        a = b
        b = a+c


        print(a+b)



# def fib(n):
#     prevnum = 0
#     currentnum = 1
#     for i in range(1,n):
#         preprenum = prevnum
#         prevnum = currentnum
#         currentnum = preprenum+prevnum
#     return currentnum
