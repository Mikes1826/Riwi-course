# formula n! = n x (n-1) x (n-2)


def facto ():
    try:
        num = int(input("factorial de "))

        if num < 0:
            print("x NO EXISTEN FACTORIALES NEGATIVOS")
        if num == 0:
            print(f"{num}! = 1")

        resultado = 1
        proceso = []
        for i in range(1, num + 1):
            resultado *= i
            proceso.append(str(i))

        return f":D {num}! = {' x '.join(proceso)} = {resultado}"
    except ValueError:
        return("ingrese un valor numerico")

print(facto())