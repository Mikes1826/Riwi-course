

# this function adds products to the inventory
def addProduct():
    storage = {'Items' : {}} #here we store all items
    loop = True
    while loop: # main loop to add multiple items
        option = input('Type "add" to add item or "quit" to finish: ').lower()
        if option == 'add':
            itemName = input('Enter item name: ')
            itemValue = int(input('Enter item value per unit: '))
            itemQuantity = int(input('Enter item quantity: '))
            storage['Items'][itemName]= {'Item Name': itemName, 'Item Value': itemValue, 'Item Quantity': itemQuantity} # Storing item details in a nested dictionary
            continue
        elif option == 'quit':
            loop = False
        else:
            print('Invalid option')
            continue
        return storage

def showInventory(storage): # function to display current inventory
    print('Current Inventory Stock')
    for item in storage['Items'].values():
        print(f"Item Name: {item['Item Name']}, Item Value: {item['Item Value']}, Item Quantity: {item['Item Quantity']}")

def stadisitcs(storage): # function to calculate and display inventory statistics
    totalValue = 0
    totalItems = 0
    for item in storage['Items'].values():
        totalValue += item['Item Value'] * item['Item Quantity'] # calculating total value
        totalItems += item['Item Quantity']
    print(f'Total Inventory Value: {totalValue}')
    print(f'Total Number of Items: {totalItems}')

def inventoryApp():# main function to run the inventory application
    loop = True
    while loop:
        option = input(
            '----------INVENTORY----------\nType "add" to add product\n "show" to display inventory\n "stats" for statistics\n  "quit" to exit\n Answer: '
            ).lower()
        if option == 'add':
            storage = addProduct()
        elif option == 'show':
            showInventory(storage)
        elif option == 'stats':
            stadisitcs(storage)
        elif option == 'quit':
            loop = False
        else:
            print('Invalid option')

inventoryApp()

#This code simulates a inventory management system where users can add products, view current inventory, and see statistics about the inventory.