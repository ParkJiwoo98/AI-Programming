f1 = open("Names.txt", 'r')
names = f1.readlines()
f1.close()
for i in range(0, len(names)):
    names[i] = names[i].rstrip()

number = int(input('How many names? '))
addName = []
for i in range(0, number):
    addName.append(str(input('Enter a name: ')))

names = names + addName
for i in range(0, len(addName)):
    if names.count(addName[i]) != 1:
        print('{} is overlapped.'.format(addName[i]))

nameSet = set(names)
names = list(nameSet)
names.sort()

for i in range(0, len(addName)):
    nameIndex = names.index(addName[i])
    if nameIndex == 0:
        print('{0:<9} -> {1:<9} -> {2:<9}'.format('X', names[nameIndex], names[nameIndex + 1]))
    elif nameIndex == len(addName) - 1:
        print('{0:<9} -> {1:<9} -> {2:<9}'.format(names[nameIndex - 1], names[nameIndex]), 'X')
    else:
        print('{0:<9} -> {1:<9} -> {2:<9}'.format(names[nameIndex - 1], names[nameIndex], names[nameIndex + 1]))

f2 = open("Names.txt", 'w')
for i in range(0, len(names)):
    f2.writelines(names[i] + '\n')
