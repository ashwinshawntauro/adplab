stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    totalqtn=0
    for item,quantity in inventory.items():
        totalqtn=totalqtn+quantity
        print(str(quantity),' ',item)
    print('Total number of items: ',str(totalqtn))

displayInventory(stuff)

def addToInv(inventory,addeditem):
    for item in addeditem:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory

dragonloot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInv(stuff,dragonloot)
displayInventory(inv)