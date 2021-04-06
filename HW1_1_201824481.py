sentence = str(input('Enter a sentence: '))
word = str(input('Enter word to replace: '))
replacement = str(input('Enter replacement word: '))
index = sentence.find(word)
newSentence = sentence[:index] + replacement + sentence[index + len(word):]
print(newSentence)