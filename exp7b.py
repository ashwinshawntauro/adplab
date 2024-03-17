import sys,re
def checkphone(phone):
    return phone.isdigit() and len(phone)==10

def checkpassword(password):
    flag=0
    if not re.search('[0-9]',password):
        flag=1
    if not re.search('[a-z]',password):
        flag=1
    if not re.search('[A-Z]',password):
        flag=1
    if not re.search('[#@!$]',password):
        flag=1
    if not len(password)>6:
        flag=1
    if flag==0:
        return True
    else:
        return False

def getPassword():
    while True:
        password=input("Enter password: ")
        checkpassword(password)
        if checkpassword(password):
            print('Valid')
            break
        else:
            print('Invalid')

def getPhone():
    while True:
        phone=input("Enter phone: ")
        checkphone(phone)
        if checkphone(phone):
            print('Valid')
            break
        else:
            print('Invalid')

print('Students enter phone number and password:\n')
ch='y'
while ch=='y' or ch=='Y':
    getPassword()
    getPhone()
    ch=input('Do you want to continue: ')