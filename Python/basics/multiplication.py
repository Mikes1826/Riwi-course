def multiplicationTable():
    num = int(input("insert a number: "))
    i = 0
    while i <= 10:
        multiplication = num * i
        print(f"{i} multiplied by {num} = {multiplication}")
        i = i + 1

multiplicationTable()