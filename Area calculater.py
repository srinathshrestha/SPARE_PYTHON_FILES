import  math
pi = math.pi
def circle(radious):
    return pi*radious**2

def cube(side):
    return side**3

def cylinder(height,radious):
    return 2*pi*radious+2*pi*height

def sphere(radiou):
    return 2*pi*(radiou**2)
print('CHOSE ONE OF THE FOLLOWING : ')
print(' circle \n cube \n cylinder \n sphere')
opt=str(input('---->> '))
if opt == 'circle':
    n = int(input('Enter the radious : '))
    print(f'AREA of the {opt} is',circle(n),'cubic unit')
elif opt == 'cube':
    n = int(input('Enter the side : '))
    print(f'AREA of the {opt} is',cube(n),'cubic unit')
elif opt == 'cylinder':
    n = int(input('Enter the height : '))
    a = int(input('Enter the radious : '))
    print(f'AREA of the {opt} is',cylinder(n,a),'cubic unit')
elif opt == 'sphere':
    n = int(input('Enter the radious : '))
    print(f'AREA of the {opt} is',sphere(n),'cubic unit')
















