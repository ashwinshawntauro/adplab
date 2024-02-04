def square(side):
    area_sqr=side*side
    print('Area of the square is ',area_sqr)

def rectangle(l,b):
    area_rect=l*b
    print('Area of the rectangle is ',area_rect)

def circle(r):
    area_crl=3.14*r*r
    print('Area of circle is ',area_crl)

print('1.Area of square\n2.Area of rectangle\n3.Area of Circle\n')
ch=int(input('Choose an option:'))
if(ch==1):
    side=int(input('Enter the side:'))
    square(side)
elif(ch==2):
    l=int(input('Enter the length'))
    b=int(input('Enter the breadth'))
    rectangle(l,b)
elif(ch==3):
    r=int(input('Enter the radius'))
    circle(r)
else:
    print('Invalid choice')
