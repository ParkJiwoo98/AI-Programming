sentence = str(input('Enter a sentence: '))
i = 0
j = 0
while sentence[i] != ' ':
    i += 1
print('First word: ', end='')
while j < i:
    print(sentence[j], end='')
    j += 1
print('')
i = len(sentence) - 2
while sentence[i] != ' ':
    i -= 1
i += 1
print('Last word: ', end='')
while i < len(sentence) - 1:
    print(sentence[i], end='')
    i += 1
print('')