def wordMult():
    word = input("Insert a word: ")
    num = int(input("word multiplied by: "))

    outcome = (word + " ") * num

    return outcome

print(wordMult())