def vowelsCount():
    word = input("Write a word: ").lower()
    vowels = "aeiou"
    count = 0
    for vowel in word:
        if vowel in vowels:
            count += 1
    print (f"This word {word} has {count} vowels")

vowelsCount()