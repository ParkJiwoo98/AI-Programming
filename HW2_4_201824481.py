erase = ['N', 'I', 'N', 'E', 'L', 'E', 'T', 'T', 'E', 'R', 'S']
startingWord = str(input('Starting word: '))
crossedOutLetters = []
remainingLetters = list(startingWord)
i = 0
while erase:
    if startingWord[i] in erase:
        erase.remove(startingWord[i])
        crossedOutLetters.append(startingWord[i])
        remainingLetters.remove(startingWord[i])
    i += 1
i = 0
print('Crossed out letters: ', end='')
while i < len(crossedOutLetters):
    print(crossedOutLetters[i], '', end='')
    i += 1
print()
i = 0
print('Remaining letters: ', end='')
while i < len(remainingLetters):
    print(remainingLetters[i], '', end='')
    i += 1
print()