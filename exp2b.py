def circle():
    r=int(input('Enter the radius'))
    area=3.14*r*r
    print(area)

def rect():
    l=int(input('Enter length'))
    b=int(input('Enter breadth'))
    area=l*b
    print(area)

def square():
    s=int(input('Enter side'))
    area=s*s
    print(area)

print('1.Circle\n2.Rectangle\n3.Square\n')
ch=int(input("Enter your choice"))
if(ch==1):
    circle()
elif(ch==2):
    rect()
elif(ch==3):
    square()
else:
    print('Invalid')