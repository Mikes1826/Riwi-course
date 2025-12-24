import json
import csv
import os
import validations as val

storage = {'Devices':[
    {
        'deviceID' : 0,
        'deviceName' : 'Laptop Dell XPS',
        'category' : 'Laptop',
        'currentStatus' : 'AVAILABLE',
        'registerDay' :  '12/05/2025',
        'description' : 'This device its amazing, its fantastic it makes me fell Supercalifragilisticexpialidocious'
    },
    {
        'deviceID' : 1,
        'deviceName' : 'Laptop lenovo',
        'category' : 'Laptop',
        'currentStatus' : 'AVAILABLE',
        'registerDay' :  '12/05/2025',
        'description' : 'This device its amazing, its fantastic it makes me fell Supercalifragilisticexpialidocious'
    },
]}

def createFile():
    fileName = input('Insert File Name: ')
    route = f'./files/{fileName}.json'
    with open(route, 'w') as file:
        json.dump(storage, file, indent=2)
    return route

def readData(route):
    with open(route, 'r') as file:
        data = json.load(file)
        return data


def loadData():
    fileName = input('Inser file name: ')
    route = val.fileValidation(fileName)
    return route

def logIn():
        data = val.isThereAUser()
        attempt = 3
        while attempt > 0:
            user = input('Insert User to log in: ')
            password =  val.passwordValidation()
            if password == data['password'] and user == data['user']:
                print('Log in succesfully!!!!')
                isLogin = True
                return isLogin
            else:
                print('Wrong password :c try again')
                attempt -= 1
            continue
        if attempt == 0:
            print(f'There is {attempt} attempts try later')


def addDevice(route):
    id = int(input('Insert device ID: '))
    name = input('Insert device name: ')
    category = input('Insert category: ')
    status = input('insert status: ')
    registerDate = input('Insert registration date: ')
    description = input('Insert a short description: ')
    newDevice = {'deviceID' : id, 'deviceName' : name, 'category' : category, 'currentStatus' : status, 'registerDay' :  registerDate, 'description' : description}
    with open(route, 'w') as file:
        storage['Devices'].append(newDevice)
        json.dump(storage, file, indent=2)

def updateDevice(route, data):
    name = input('Insert device name to update: ')
    for i, value in enumerate(data['Devices']):
        if name == value['deviceName']:
            newName = input('Insert new name: ')
            newCategory = input('Insert new category: ')
            newStatus = input('insert new status: ')
            registerDate = input('Insert new registration date: ')
            description = input('Insert new description: ')
            data['Devices'][i]['deviceName'] = newName
            data['Devices'][i]['category'] = newCategory
            data['Devices'][i]['currentStatus'] = newStatus
            data['Devices'][i]['registerDay'] = registerDate
            data['Devices'][i]['description'] = description
        with open(route, 'w') as file:
            json.dump(storage, file, indent=2)

def deleteDevice(route, data):
    """Delete a device by ID"""
    try:
        device_id = int(input('Insert device ID to delete: '))
        device_found = False
        for i, value in enumerate(data['Devices']):
            if device_id == value['deviceID']:
                device_found = True
                device_name = value['deviceName']
                # Confirm deletion
                confirm = input(f"Are you sure you want to delete '{device_name}'? (yes/no): ")
                if confirm.lower() == 'yes':
                    del data['Devices'][i]
                    # Write back to file
                    with open(route, 'w') as file:
                        json.dump(data, file, indent=2)
                    print(f"Device '{device_name}' deleted successfully!")
                else:
                    print("Deletion cancelled.")
                break
        if not device_found:
            print(f"Device with ID {device_id} not found!")
    except ValueError:
        print("Please enter a valid numeric ID.")


def exportCSV(fileName, data):
    if not data['Devices']:
        print("No devices to export.")
        return None
    routeCSV = f'./files/{fileName}.csv'
    try:
        with open(routeCSV, 'w', newline='') as file:
            fieldnames = data['Devices'][0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data['Devices'])
        print(f"Data exported successfully to {fileName}.csv")
        return routeCSV
    except Exception as e:
        print(f"Error exporting CSV: {e}")
        return None

def importCSV():
    name = input('Insert CSV file name (without extension): ')
    route = f'./files/{name}.csv'
    if not os.path.exists(route):
        print(f"File '{name}.csv' not found!")
        return None
    try:
        with open(route, 'r') as file:
            csvfile = csv.DictReader(file)
            devices = list(csvfile)
        print(f"Successfully imported {len(devices)} devices from CSV")
        return {'Devices': devices}
    except Exception as e:
        print(f"Error importing CSV: {e}")
        return None
