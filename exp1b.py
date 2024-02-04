def compare(num1,num2):
    if(num1 == num2):
        print(num1,' and ',num2,' are equal')
    elif(num1>num2):
        print(num1,' is greater than ',num2)
    else:
        print(num2,' is greater than ',num1)

num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
compare(num1,num2)