count = int(input('How many numbers do you want to enter? '))
number = []
median = 0.0
i = 0
while i < count:
    number.append(int(input('Enter a number: ')))
    i += 1
number.sort()
if count % 2 == 0:
    median1 = number[count // 2]
    median2 = number[count // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = number[count//2]
print('Median:', median)