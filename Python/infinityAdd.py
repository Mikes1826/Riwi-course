def infinityAdd():
    i = 1
    add = 0
    while i != 0:
        num = int(input("Insert a number to add: "))
        add = add + num
        print(f"Current  total: {add}")
        if num == 0:
            i = 0
    return f"Total sum {add}"

print(infinityAdd())
