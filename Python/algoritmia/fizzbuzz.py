def fizzbuzz():
    listNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    newListNum =[]

    for i in listNum:
        if i % 3 == 0 and i % 5 == 0:
            newListNum.append("FizzBuzz")
        elif i % 3 == 0:
            newListNum.append("Fizz")
        elif i % 5 == 0:
            newListNum.append("Buzz")
        else:
            newListNum.append(i)
    return newListNum

print(fizzbuzz())