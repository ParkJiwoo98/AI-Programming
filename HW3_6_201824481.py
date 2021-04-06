print('UNITS OF LENGTH')
print('{0:<12}{1:<12}{2:<12}'.format('inches', 'feet', 'miles'))
print('{0:<12}{1:<12}{2:<12}'.format('meters', 'fathoms', 'yards'))
print('{0:<12}{1:<12}{2:<12}'.format('kilometers', 'furlongs', 'rods'))
print()

unitFrom = str(input('Unit to convert from: '))
unitTo = str(input('Unit to convert to: '))
value = int(input('Enter length in {}: '.format(unitFrom)))

file = open("Units.txt", 'r')
unit = []
lines = file.readlines()
file.close()

for i in range (0, len(lines)):
    lines[i] = lines[i].rstrip()

fromFeet = ''
toFeet = ''
for i in range(0, len(lines)):
    j = 0
    while j < len(unitFrom):
        if lines[i][j] != unitFrom[j]:
            break
        j += 1
    if j == len(unitFrom):
        for k in range(lines[i].index(',') + 1, len(lines[i])):
            fromFeet += lines[i][k]
        break
fromFeet = float(fromFeet)

for i in range(0, len(lines)):
    j = 0
    while j < len(unitTo):
        if lines[i][j] != unitTo[j]:
            break
        j += 1
    if j == len(unitTo):
        for k in range(lines[i].index(',') + 1, len(lines[i])):
            toFeet += lines[i][k]
        break
toFeet = float(toFeet)

feet = value * fromFeet
changedValue = feet / toFeet

print('Length in {}: {:.4f}'.format(unitTo, changedValue))