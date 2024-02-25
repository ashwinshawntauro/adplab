import sys,re
def check_num(number):
    if re.match('[0-9]{10}',number):
        return True
def check_pass(password):
    if re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#!]).{8,}$',password):
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