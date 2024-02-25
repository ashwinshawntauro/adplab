import sys,pyperclip
password={'email':'ash@gmail.com','blog':'abc blog','luggage':'1234'}
if(len(sys.argv)<2):
    print("Usage:py pw.py[account]")
    sys.exit()
account=sys.argv[1]
print(sys.argv[1])
if account in password:
    pyperclip.copy(password[account])
    print('Password of ',account,' copied to clipboard')
else:
    print('Password does not exists')
