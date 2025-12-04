

def fibo():

    n = int(input("Insert a number: "))
    if n <= 1:
        return f"The number its just {n}"

    secuencce = []

    a, b = 0, 1
    for i in range(2, n + 1):
        nextFib = a + b
        a = b
        b = nextFib
        secuencce.append(b)
    return secuencce

print(fibo())
