import storage as st


def app():

    isLogin = st.logIn()
    loop = isLogin
    while loop:
        try:
            print('====================== \n =====INVENTORY===== \n ====================== \n                   ')
            print('What do you want to do? \n 0. Load Data\n 1. Create new inventory\n 2. Add new device\n 3. Delete device\n 4.Update device \n 5. Show inventory\n 6. Export as CSV\n 7.Upload CSV \n 8. Exit')
            option = int(input('Option: '))
            if option == 0:
                route = st.loadData()
                data = st.readData(route)
                continue
            elif option == 1:
                route = st.createFile()
                data = st.readData(route)
                continue
            elif option == 2:
                st.addDevice(route)
                continue
            elif option == 3:
                st.deleteDevice(route, data)
                continue
            elif option == 4:
                st.updateDevice(route,data)
                continue
            elif option == 5:
                for item in data['Devices']:
                    print(item)
                continue
            elif option == 6:
                st.exportCSV()
                continue
            elif option == 7:
                st.importCSV()
                continue
            elif option == 8:
                isLogin = False
                break
            else:
                print('Option not available :c')
        except ValueError:
            print('Select a correct option!')
app()