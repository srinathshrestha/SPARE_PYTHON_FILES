# palindrome : its same from front and back
# M A D A M ====(form backward)======= M A D A M
# cheaking is a no/sequ/str is palindrome or not
def palindrome(p):
    x = p[::-1]
    if x==p :
        return (f'{p} is a palindrome')
    else:
        return (f'{p} is a not a palindrome')
a=palindrome(input("Enter your str or number or sequence : \n"))
# --------------------------------------------------------------------------------------------


print(a)