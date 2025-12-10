def biggerElement():
    large = int(input("How large is your list?: "))
    list = []
    bigger = 0
    for i in range(large):
        num = int(input(f"Inserte number on position {i} "))

        list.append(num)

    for i in range(len(list)):
        if list[i] < list[i]:
            bigger = list[i]
    return bigger
print(biggerElement())