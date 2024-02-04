def add(x,y):
    result=x+y
    print('Result: ',result)
def sub(x,y):
    result=x-y
    print('Result: ',result)
def mult(x,y):
    print('Result: ',x*y)
def div(x,y):
    if(y>0):
        print('Result: ',x/y)
    else:
        print('Invalid')
print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n')
ch=int(input('Choose any operation: '))
x=float(input('Enter first number '))
y=float(input('Enter second number '))
if(ch==1):
    add(x,y)
elif(ch==2):
    sub(x,y)
elif(ch==3):
    mult(x,y)
if(ch==4):
    div(x,y)
else:
    print('Invalid choice')
