def sumPairs():
    listNum = [1,2,3,4,5,6,7,8,9,10]
    totalSum = 0

    for i in listNum:
        if i % 2 == 0:
            totalSum += i
    return f"This is the total {totalSum}"

print(sumPairs() )
