birthdate={'alice':'apr 1','rohan':'jun 14','bob':'aug 23'}
while True:
    name=input('Enter the name to find birthday (blank to quit): ')
    if(name==''):
        break
    else:
        if name in birthdate:
            print(str(birthdate[name]+ ' is the birthdate of '+name))
        else:
            print('When is the birthday of ',name)
            bdate=input()
            birthdate[name]=bdate
            print('Birthday database updated')

