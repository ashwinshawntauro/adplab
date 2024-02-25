import sys,re
def check_num(number):
    return number.isdigit() and len(number)==10
def check_pass(password):
    flag=0
    if not re.search('[0-9]',password):
        flag=1
    if not re.search('[a-z]',password):
        flag=1
    if not re.search('[A-Z]',password):
        flag=1
    if not re.search('[#$@!]',password):
        flag=1    
    if flag==1:
        return False
    else:
        return True

def phonenum():
    while True:
        number=input('Enter the phone number: ')
        if check_num(number):
            print('...Valid Phone number')
            break
        else:
            print('Invalid phone number')
    

def passw():
    while True:
        password=input('Enter the password: ')
        if check_pass(password):
            print('...Valid Password')
            break
        else:
            print('Invalid Password')

print('Studen Registration:\n')
ans='y'
while ans=='y' or ans=='Y':
    phonenum()
    passw()
    ans=input('Do you want to continue?')