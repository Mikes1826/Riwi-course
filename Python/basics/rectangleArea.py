def rectangleArea():
    height = float(input("What's the rectangle height?: "))
    base = float(input("What's the rectangle base?: "))

    rectangleArea = base * height

    return f"The reactangle's area its {rectangleArea}"

print(rectangleArea())
