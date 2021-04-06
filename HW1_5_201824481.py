ranges = str(input())
start = ranges[5 : ranges.find('to') - 1]
end = ranges[ranges.find('to') + 3 :]
startNum = 0
endNum = 0
if start.isdigit():
    startNum = int(start)
else:
    while start != '':
        if start[:3] == 'one':
            startNum = 1
            if len(start) != 3:
                start = start[4:]
            else:
                start = ''
        elif start[:3] == 'two':
            startNum = 2
            if len(start) != 3:
                start = start[4:]
            else:
                start = ''
        elif start[:5] == 'three':
            startNum = 3
            if len(start) != 5:
                start = start[6:]
            else:
                start = ''
        elif start[:4] == 'four':
            startNum = 4
            if len(start) != 4:
                start = start[5:]
            else:
                start = ''
        elif start[:4] == 'five':
            startNum = 5
            if len(start) != 4:
                start = start[5:]
            else:
                start = ''
        elif start[:3] == 'six':
            startNum = 6
            if len(start) != 3:
                start = start[4:]
            else:
                start = ''
        elif start[:5] == 'seven':
            startNum = 7
            if len(start) != 5:
                start = start[6:]
            else:
                start = ''
        elif start[:5] == 'eight':
            startNum = 8
            if len(start) != 5:
                start = start[6:]
            else:
                start = ''
        elif start[:4] == 'nine':
            startNum = 9
            if len(start) != 4:
                start = start[5:]
            else:
                start = ''
        elif start[:7] == 'million':
            startNum = startNum * 1000000
            if len(start) != 7:
                start = start[8:]
            else:
                start = ''

if end.isdigit():
    endNum = int(end)
else:
    while end != '':
        if end[:3] == 'one':
            endNum = 1
            if len(end) != 3:
                end = end[4:]
            else:
                end = ''
        elif end[:3] == 'two':
            endNum = 2
            if len(end) != 3:
                end = end[4:]
            else:
                end = ''
        elif end[:5] == 'three':
            endNum = 3
            if len(end) != 5:
                end = end[6:]
            else:
                end = ''
        elif end[:4] == 'four':
            endNum = 4
            if len(end) != 4:
                end = end[5:]
            else:
                end = ''
        elif end[:4] == 'five':
            endNum = 5
            if len(end) != 4:
                end = end[5:]
            else:
                end = ''
        elif end[:3] == 'six':
            endNum = 6
            if len(end) != 3:
                end = end[4:]
            else:
                end = ''
        elif end[:5] == 'seven':
            endNum = 7
            if len(end) != 5:
                end = end[6:]
            else:
                end = ''
        elif end[:5] == 'eight':
            endNum = 8
            if len(end) != 5:
                end = end[6:]
            else:
                end = ''
        elif end[:4] == 'nine':
            endNum = 9
            if len(end) != 4:
                end = end[5:]
            else:
                end = ''
        elif end[:7] == 'million':
            endNum = endNum * 1000000
            if len(end) != 7:
                end = end[8:]
            else:
                end = ''
i = startNum
result = 0
while i <= endNum:
    j = i
    while j != 0:
        result += j % 10
        j //= 10
    i += 1
print('The sum of the digits in the numbers')
print(ranges, 'is {:,}.'.format(result))