def Compare():
    num1 = int(input("Insert the first number: "))
    num2 = int(input("Insert the second number: "))

    if num1 > num2:
        return f"This number {num1} It's bigger than this one {num2}"
    elif num1 < num2:
        return f"This number {num1} It's fewer than this one {num1}"
    else:
        return f"Both of these numbers are equals!!"

print(Compare())