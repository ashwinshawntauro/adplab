import sys,pyperclip

password={'email':'abc@gmail.com','number':'23333','luggage':'abcd'}

if(len(sys.argv)<2):
    print('Invalid input')
    sys.exit()

account=sys.argv[1]
print(account)
if account in password:
    pyperclip.copy(password[account])
    print('Password copied of ',account)
else:
    print(account,' not present in password')