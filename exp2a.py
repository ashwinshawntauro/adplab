num=int(input('Enter a number'))
fact=1
if(num<0):
        print('Factorial not possible')
elif(num==0 or num==1):
    print('Factorial is 1')
else:
    for i in range(1,num+1):
        fact=fact*i
    print('Factorial is ',fact)
