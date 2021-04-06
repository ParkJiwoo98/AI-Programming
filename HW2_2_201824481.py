name = str(input('Enter a 3-part name: '))
i = 0
while name[i] != ' ':
    i += 1
i += 1
print('Middle name: ', end='')
while name[i] != ' ':
    print(name[i], end='')
    i += 1
print('')