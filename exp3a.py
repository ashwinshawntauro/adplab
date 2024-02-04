import random
secretNum=random.randint(1,20)
print('I am thinking of a number between 1 and 20')
for guessTaken in range(7):
    num=int(input('Take a guess'))
    if(num<secretNum):
        print('Your guess is too low')
    elif(num>secretNum):
        print('Your guess is too high')
    else:
        break
if(num==secretNum):
    print('Good Job! you guessed it in ',guessTaken,' guessed')
else:
    print('The number I was thinking is ',secretNum)
