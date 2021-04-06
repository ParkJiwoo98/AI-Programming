import random

result = ['Head', 'Tail']
head = 0
for i in range(0, 100):
    if random.choice(result) == 'Head':
        head += 1
print('Head occurs {} times.'.format(head))