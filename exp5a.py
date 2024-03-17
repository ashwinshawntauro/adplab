allGuests={'alice':{'apple':5,'pretzels':12},'bob':{'ham sandwiches':3,'apples':2},'carol':{'cups':3,'apple pies':1}}

def totalBrought(guests,item):
    numBrought=0
    for guest,guestitem in guests.items():
        numBrought=numBrought+guestitem.get(item,0)
    return numBrought

print('The total number of items: ')
print('Apple - ',str(totalBrought(allGuests,'apple')))
print('pretzels - ',str(totalBrought(allGuests,'pretzels')))
print('cake - ',str(totalBrought(allGuests,'cake')))
print('ham sandwiches - ',str(totalBrought(allGuests,'ham sandwiches')))