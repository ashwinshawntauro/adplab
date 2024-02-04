stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    count=0
    for item,quantity in inventory.items():
        print(str(quantity)+' '+item)
        count=count+quantity
    print('total quantity',count)
displayInventory(stuff)
def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(stuff,dragonLoot)
displayInventory(inv)