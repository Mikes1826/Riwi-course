# Casos Especiales
# 1: NO es primo (solo tiene un divisor)

# 2: Es el ÚNICO número primo par

# 0: NO es primo (no es mayor que 1)



def isPrime():
    num = int(input("Insert a number: "))

    if num < 2:
        print(f"{num} It's not prime X. (it's less than 1)")
    elif num == 2:
        print(f"{num} the only even prime number")
    elif num % 2 == 0:
        print(f"{num} Its not prime, this number its pair and its not 2")
        return
    limit = int(num**0.5) + 1
    print(f"√{num} = {num**0.5:.2f}")
    print(f"validating dividers until {limit-1}")

    for divider in range(3, limit,2): #3 - Start value (first number in the sequence) limite - Stop value (loop goes up to, but does not include, this number) 2 - Step value (increment between numbers)
        outcome = num / divider
        if num % divider == 0:
            print(f"{num} / {divider} = {outcome} -> Divisible X")
            print (f"Is not prime :C it divisible by {divider}")
            return
        else:
            print(f"{num} / {divider} = {outcome:.2f} -> not Divisible √")
    print(f"Ist PRIME :DDDDD")
isPrime()