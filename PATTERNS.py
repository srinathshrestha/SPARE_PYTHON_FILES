# print('* '*4)
# print('* '*4)
# print('* '*4)
# print('* '*4)
n=int(input("Enter the number of the row you want : "))
#----------------------SQUARE-------------------------------
for i in range (n):
        print('* '*n)

#--------------------------ARROW .R>L--------------------------------
for i in range(1,n+1):
    print('* '*i)
for i in range(n-1,0,-1):
    print('* '*i)


for i in range(1,n+1):
    print('  '*(n-i)+'* '*i)


# ------------------ARROW R>L---------------------------
for i in range(1,n+1):
    print('    '*(n-i)+'*   '*i)
for i in range(n-1,0,-1):
    print('    '*(n-i)+'*   '*i)
# --------------------------DIMOND-----------------
for i in range(1,n+1):
    print('  '*(n-i)+'*   '*i)
for i in range(n-1,0,-1):
    print('  '*(n-i)+'*   '*i)


