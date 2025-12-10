

# this function set the item name using a while loop to handle errors
def setName():
    #I used while loop to handle some errors that could happen during the program execution
    while True:
        name = input("Insert a item name: ").strip()
        if name == "":
            print("The item's name is empty")
            continue
        elif len(name) < 2:
            print("The item name must have more than 2 characters")
            continue
        elif len(name) > 100:
            print("The item's name is too large! max 100 characters")
            continue
        return name

# This function set a quantity of items, we use try to handle values errors
def setQuantity():
        while True:
            try:
                quantity = int(input("Insert a item quantity: "))
                if quantity == 0:
                    print("The item's quantity is empty")
                    continue
                elif quantity < 0 :
                    print("The item quantity must be positive ... a mean you know items in negative ... is weird")
                    continue
                return quantity
            except ValueError:
                print(f"Use only numbers to express quantity")

# This function set the price of items, we use try to handle values errors
def setValue():
            while True:
                try:
                    value = float(input("Insert a item price: "))
                    if value == 0:
                        print("The item's value is empty")
                        continue
                    elif value < 0 :
                        print("The item value must be positive ... a mean you know items in negative ... is weird")
                        continue
                    return value
                except ValueError:
                    print(f"Use only numbers to express value")


# This function return the total amout between the value multiplied by the quantity
def total(value, quantity):
    totalAmount = value * quantity
    return totalAmount

##This function initialized the program

def inventoryApp():
    option = int(input(f"Select an option: \n 1. Buy something \n 0. Exit \n Enter: "))
    while option != 0:
        itemName = setName()
        itemQuantity = setQuantity()
        itemValue = setValue()
        TotalAmount = total(itemValue, itemQuantity)

        print(f"{'='*50}")
        print(f"Item: {itemName}")
        print(f"Quantity: {itemQuantity}")
        print(f"Item price: {itemValue}")
        print("------------------------")
        print(f"Total: {TotalAmount}")
        print("------------------------")
        print("Thanks for buying here !")
        option = 0

inventoryApp()

#This program is a siulation of a online shoping here we can add an item by its name, its value and a quantity of the item, this program handle some possibles issues tha could appear durinf the execution at the end of the program we can se a sumerize about the item, its value, the quantity and finally the total amount

