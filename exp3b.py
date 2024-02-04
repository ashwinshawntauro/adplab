import sys
def collatz(num):
    if(num%2==0):
        value=num//2
    else:
        value=num*3+1
    while value==1:
        print(value)
        sys.exit()
    while value!=1:
        print(value)
        num=value
        return collatz(num)

print('Enter a starting number(greater than 0) or quit:')
num=input('>')
if (num==0 or not num.isdecimal()):
    print('Enter a positive integer greater than 0')
else:
    collatz(int(num))