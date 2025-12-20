import json


data = {    'Students': [
        {
            'Name' : 'Ernesto Frailejon',
            'ID' : '123456',
            'Subjects' : ['Math', 'Philosophy', 'Python']
        },
        {
            'Name' : 'Michael Jackson',
            'ID' : '654321',
            'Subjects' : ['Hehe', 'moonwalk', 'smooth Criminal']
        }
    ]
}



def createFile():
    file = input('File name: ')
    route = f'./files/{file}'
    with open(route,'w') as studentFile:
        json.dump(data, studentFile, indent=2)
    return route

route = createFile()

def readData():
    try:
        with open(route, 'r') as studentFile:
            list = studentFile.read()
            print(list)
    except FileNotFoundError:
        print('Create the file')


def writeData():
    studentName = input('Insert Student Name: ')
    studentID = input('Insert Student ID: ')
    studentsubject = []
    subject = True
    while subject :
        option = int(input('1. Add estuden subject\n2. no more\n Option: '))
        if option == 1:
            subjectName = input('Insert subject Name: ')
            studentsubject.append(subjectName)
            continue
        elif option == 2:
            subject = False
        else:
            print('Invalid option')
    return studentName, studentID, studentsubject

def setData():
    studentsName , stundetId, studentSub = writeData()
    newStudent = {
        'Name' : studentsName,
        'ID' : stundetId,
        'Subjects' : studentSub
        }
    with open(route, 'w') as studentFile:
        data['Students'].append(newStudent)
        json.dump(data, studentFile, indent=2)

def updateData():
    with open(route, 'r') as studentFile:
        data = json.load(studentFile)
        studentId = input('Insert student ID to update info: ')
        for student in data['Students']:
            if student['ID'] == studentId:
                print('Student found')
                newName = input('Insert new name: ')
                newSubjects = []
                subject = True
                while subject :
                    option = int(input('1. Add estuden subject\n2. no more\n Option: '))
                    if option == 1:
                        subjectName = input('Insert subject Name: ')
                        newSubjects.append(subjectName)
                        continue
                    elif option == 2:
                        subject = False
                    else:
                        print('Invalid option')
                student['Subjects'] = newSubjects
                student['Name'] = newName
                with open(route, 'w') as studentFile:
                    json.dump(data, studentFile, indent=2)
                print('Student info updated')
                return
        print('Student not found')

def deleteData():
    with open(route, 'r') as studentFile:
        data = json.load(studentFile)
        studentId = input('Insert student ID to delete info: ')
        for i, student in enumerate(data['Students']):
            if student['ID'] == studentId:
                print('Student found')
                del data['Students'][i]
                with open(route, 'w') as studentFile:
                    json.dump(data, studentFile, indent=2)
                print('Student info deleted')
                return
        print('Student not found')
