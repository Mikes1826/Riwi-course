# (0 °C × 9/5) + 32 = 32 °F

def fahrenheit():
    celsius = float(input("How many celsius degrees you want to convert?: "))
    fahrenheit = (celsius  * 9/5) + 32

    return fahrenheit

print(fahrenheit())