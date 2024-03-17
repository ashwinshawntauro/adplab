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
        collatz(num)

print("Enter a starting number")
res=input('>')
if(res=='0' and not res.isdigit()):
    print("Must be greater than 0 or positive integer")
else:
    num=int(res)
    print(num)
    while num==1:
        print('Input must be greater than 1')
        sys.exit()
    collatz(num)