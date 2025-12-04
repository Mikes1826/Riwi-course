def leapYear():
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "It's a leap year :D"
            else:
                return "It's not a leap  year :C"
        else:
            return "It's a leap year :D"
    else:
        return "It's not a leap  year :C"
print(leapYear())