def isPositive():
    num = int(input("Insert a number: "))
    if num >= 0:
        return F"The number {num} is positive!"
    else:
        return F"The number {num} is not positive!"

print(isPositive())