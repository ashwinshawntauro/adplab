def swap(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print('Swapped numbers are: ',num1,num2)

num1=int(input('Enter first number '))
num2=int(input('Enter second number '))
swap(num1,num2)