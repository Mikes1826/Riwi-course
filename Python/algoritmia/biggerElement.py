def bigger():
    number = [1,6,2,35,50,-999]
    biggernum = number[0]
    for i in number:
        if biggernum < i:
            biggernum = i
    return f"between these number {number} this one is the bigger {biggernum}"
print(bigger())
