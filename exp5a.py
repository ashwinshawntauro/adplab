allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guest, item):
    total=0
    for guestname,guestitem in guest.items():
        total=total+guestitem.get(item,0)
    return total

print('-apples '+str(totalBrought(allGuests,'apples')))
print('-ham sandwiches '+str(totalBrought(allGuests,'ham sandwiches')))
print('-mango '+str(totalBrought(allGuests,'mango')))
