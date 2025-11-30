
def reverseString():
    phrase = input("Insert a phrase: ")
    reversePhrase = "" .join(reversed(phrase))
    return reversePhrase

print(reverseString())

