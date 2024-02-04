num=int(input('Enter a number: '))
if(num==0 or num==1):
    print('Number is neither prime nor composite')
else:
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if(count==2):
        print(num,' is prime number')
    else:
        print(num,' is a composite number')
    