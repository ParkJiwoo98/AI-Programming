f = open("SomeMonths.txt", 'r')
lines = f.readlines()
f.close()

withR = []
withoutR = []

for i in range(0, len(lines)):
    lines[i] = lines[i].rstrip()
    j = 0
    wordLength = len(lines[i])
    while j < wordLength:
        if lines[i][j] == 'r':
            withR.append(lines[i])
            break
        j += 1
    if j == wordLength:
        withoutR.append(lines[i])

print('Months with r:', end=' ')
for i in range(0, len(withR)):
    print(withR[i], end=' ')
print()
print('Months without r:', end=' ')
for i in range(0, len(withoutR)):
    print(withoutR[i], end=' ')
print()