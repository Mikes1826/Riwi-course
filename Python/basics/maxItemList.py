def maxList ():
    array = []
    length = int(input("How large is your list?: "))
    for x in range(length): #range ayuda a iterar x cantidad de veces
        num = int(input(f"Enter number number {x+1}: "))
        array.append(num)
    print (max(array))
    return array
maxList()