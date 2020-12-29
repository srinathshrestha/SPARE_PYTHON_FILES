def bubble(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                t=num[j]
                num[j] = num[j+1]
                num[j+1] = t
    return num



num = []
l = int(input("Enter number of elements : "))
for i in range(0, l):
    ele = int(input('Enter the numbers : '))
    num.append(ele)

print(bubble(num))


