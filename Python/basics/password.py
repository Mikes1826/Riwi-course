def password():
    clientPassword = "python123"
    passwordInsert = input("Insert Password: ").lower()

    if passwordInsert ==  clientPassword:
        return "I know you nigga!!! :D"
    else:
        return "Who are you nigga?????? >:v"

print(password())