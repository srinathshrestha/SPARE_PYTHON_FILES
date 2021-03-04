# bigO(n) time is taken since it is a linaer search
a = [1,2,3,4,7,5,9,8]

def find(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return f"{key} is in the arry. "
        elif key != a[i]:
            return f"{key} is  not in the arry. "
print('The number list is',a)
k = int(input("Enter the number you want to find : "))
print(find(a,k))




