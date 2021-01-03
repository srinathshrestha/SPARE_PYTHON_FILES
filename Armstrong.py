a = int(input("Enter the number : \n" ))
copy_a = a
sum = 0
order = len(str(a))
while(a>0):
    d=a%10
    sum+= d ** order
    a=a//10
if (sum == copy_a):
    print(f'{copy_a} is a Armstrong number')
# else:
#     print(f'{copy_a} is not a Armstrong Number')