def palindormo():
    word = input("Insert a word: ").lower()
    reversedWord = ""
    for i in range(len(word)-1,-1,-1):
        reversedWord = reversedWord + word[i]
    if word == reversedWord:
        return f"This is a palindrome {reversedWord}"
    else:
        return f"bro... for the god sake what is this '{reversedWord}'"



print(palindormo())
