digit = int(input('Enter the digit: '))
multiple = int(input('Enter the multiple: '))
j = 1
i = 1
limit = 10
while j < digit:
    i *= 10
    limit *= 10
    j += 1
while i * multiple < limit:
    number = str(i)
    reverse = str(i * multiple)
    j = 0
    while j < digit and number[j] == reverse[digit - 1 - j]:
        j += 1
    if j == digit:
        print('Since ', digit, ' times ', number, ' is ', reverse, ',', sep='')
        print('the special number is ', number, '.', sep='')
        break
    else:
        i += 1