def wordsCounting():
    phrase = input("Insert a phrase: ")

    words = phrase.split()
    wordsAmount = len(words)
    return f"The phrase '{phrase}' has {wordsAmount} words"

print(wordsCounting())