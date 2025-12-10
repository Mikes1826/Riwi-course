def cosoEse():
    large = int(input("How large is your list?: "))
    list = []

    for i in range(large):
        num = int(input(f"Inserte number on position {i} "))

        list.append(num)

    for i in range(len(list)):
        if list[i] % 3 == 0:
            print("no")
        elif list[i] % 5 == 0:
            print("entendi") 
        elif list[i]% 5 == 0 and list[i] % 3 ==0:
            print ("no_entendi")

cosoEse()