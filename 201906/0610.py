import pprint
stuff = {'rope': 1, 'torch': 6, 'gold': 42, 'wooden dagger': 2, 'arrow': 12}

def displayInv(inventory) :
    print("")
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items() :
        print v, k
        item_total += 1
    print'Total number of items: ', str(item_total)
    return ""
print(displayInv(stuff))