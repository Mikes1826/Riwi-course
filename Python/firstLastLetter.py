
def wordsletters():

    word = input("Insert a word: ")
    wordBreakDown = []

    for i in range(len(word)):
        wordBreakDown.append(i)
    return wordBreakDown[0], wordBreakDown[-1]

print(wordsletters())