import sys
import math

isTrue = 'Yes'
num = 1
while (isTrue == 'Yes'):
    try:
        x = int(input('Enter x0 for circle 1: '))
        y = int(input('Enter y0 for circle 1: '))
        radius = int(input('Enter r0 for circle 1: '))
        x1 = int(input('Enter x1 for circle 2: '))
        y1 = int(input('Enter y1 for circle 2: '))
        radius1 = int(input('Enter r1 for circle 2: '))
        
    except ValueError:
        if (num == 3):
            print('Incorrect inputs, now exiting.')
            sys.exit()
        else:
            print('\n')
            print('Incorrect input, try again.')
            num += 1
            continue
    
    distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    
    if (distance > (radius + radius1)):
        print('The two circles do not intersect and are separate.')
        
    elif (distance < abs(radius - radius1)):
        print('The two circles do not intersect, and one is contained within the other.')
        
    elif (distance == (radius + radius1)):
        print('The two circles intersect a single point.')
        
    elif (distance == 0 and radius == radius1):
        print('The two circles are coincident.')
        
    else:
        print('The two circles intersect at two points.')
    
    isTrue = input('Do you want to continue? Enter Yes or No: ')
    
    if (isTrue == 'No'):
        print('Now exiting')
        sys.exit()