def bubble_sort(num):
    for insertion in range(len(num)-1,0,-1):
        for j in range(insertion) :
            if num[j] > num[j+1]:
                temp =  num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num



if __name__ == '__main__':


    lis = []
    num = int(input("Enter the numbers you want to sort : "))
    for i in range (0,num):
        ele = int(input())

        lis.append(ele)


    print(bubble_sort(lis))
