import random
secretNum=random.randint(1,20)
print('I am guessing a num between 1 and 20')

for guessTaken in range(1,7):
    num=int(input('Guess a number'))
    if(num<secretNum):
        print('Your guess is too low')
    elif(num>secretNum):
        print("Your guess is too high")
    else:
        break
if(num==secretNum):
    print('You guess the number in ',guessTaken)
else:
    print('Nope the number is',secretNum)
