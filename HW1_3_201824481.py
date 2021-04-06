word = str(input('Enter word to translate: '))
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    word = word + 'way'
else:
    i = 0
    for i in range(i, len(word)):
        word = word[1:] + word[0]
        if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
            break
    word = word + 'ay'
print('The word in Pig Latin is {}.'.format(word))