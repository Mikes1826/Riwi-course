import json

def passwordValidation():
    try:
        password = int(input('Isert Password: '))
        return password
    except ValueError:
        print('Please enter the numeric password!!')

def isThereAUser():
    try:
        with open('./files/users.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('File not found >:c')

def fileValidation(name):
    try:
        route = f'./files/{name}.json'
        with open(route, 'r') as file:
            json.load(file)
        return route
    except FileNotFoundError:
        print('That file doesnt exist')

