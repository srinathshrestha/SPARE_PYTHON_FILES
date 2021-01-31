num = input('Enter your YEAR OF BIRTH or AGE : ')
if len(num) == 2:
    a = int(num) + (100-int(num))
    print(f"you will turn 100 in {a} age. ")
if len(num)==4:
    a = int(num) + 100
    print(f"you will turn 100 in {a}")