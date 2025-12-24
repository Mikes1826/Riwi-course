import json
storage = {'Items' : [{
    'ID': 0,
    'Name': 'Shoes',
    'Price' : 12.36,
    'Quantity' : 3
},{
    'ID': 1,
    'Name': 'T-shirts',
    'Price' : 2.36,
    'Quantity' : 25
}
]}

def createFile():
    fileName = input('Enter the file name to create (with .json extension): ')
    route = f'./files/{fileName}'
    with open(route, 'w') as file:
        json.dump(storage, file, indent=2)
    return route



def readFile(route):
    try:
        with open(route, 'r') as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print('File not found')

def findFile(route):
    try:
        with open(route, 'r') as file:
            data = json.load(file)
        itemName = input('Enter the item name to find: ')
        for item in data['Items']:
            if itemName == item['Name']:
                print(item)
    except FileNotFoundError:
        print ('File not found')

def updateFile(route):
    try:
        with open(route, 'r') as file:
            data = json.load(file)
        itemName = input('Enter the item name to update: ')
        for item in  data['Items']:
            if itemName == file['Name']:
                item['Name'] = input('Enter new name: ')
                item['Price'] = float(input('Enter new price: '))
                item['Quantity'] = int(input('Enter new quantity'))
        with open(route, 'w') as file:
            json.dump(storage, file, indent=2)
        print(file)
    except FileNotFoundError:
        print('File not found')

