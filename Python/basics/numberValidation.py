def validation():

    num = int(input("Insert a number: "))

    if num > 0 and num <= 100:
        return f"Yeah this number {num} is between 1 and 100"
    else:
        return f"Yeah this number {num} is not between 1 and 100"
print(validation())