year = int(input('ENTER THE YEAR WHICH YOU WANTS TO CHEAK : '))

if year%400==0:
    print(f'{year} is a leap year.')
elif year%4==0:
    print(f'{year} is a leap year.')
elif year%100==0:
    print(f'{year} is not a leap year.')
else:
    print(f'{year} is not a leap year.')