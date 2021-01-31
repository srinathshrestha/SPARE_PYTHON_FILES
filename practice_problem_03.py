# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.
#
# You have to use the following three methods to reserve a list:
#
# Inbuild method of python
# List name [::-1] slicing trick
# Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]
# -------------------------------------------------------------------------------------------------------------------------
a = input('Enter the item of the list which you wants to revers with a gap <SPACE> : \n ')
list = a.split(' ')
# method one of reversing the list
revers1 = list[:]
revers1.reverse()
print(f'my 1st reversing of {list} is {revers1}')
# 2nd method of reversing the list
revers2=list[::-1]
print(f'my 2nd reversing of {list} is {revers2}')

# 3rd method of reversing the list
revers3 = list[:]
for i in range(len(revers3)//2):
    revers3[i] , revers3[len(revers3)-i-1] = revers3[len(revers3)-i-1], revers3[i]
print(f'my 3rd reversing of {list} is {revers3}')