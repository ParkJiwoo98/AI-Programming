import random
import pickle

heart = 0
diamond = 0
clover = 0
spade = 0
file = open("DeckOfCardsList.dat", 'rb')
deckOfCards = pickle.load(file)
file.close()
select = random.sample(deckOfCards, 13)
for i in range(0, 13):
    if i != 12:
        print('{}, '.format(select[i]), end='')
    else:
        print('{}'.format(select[i]))
    if select[i][-1] == '♥':
        heart += 1
    elif select[i][-1] == '♦':
        diamond += 1
    elif select[i][-1] == '♣':
        clover += 1
    else:
        spade += 1

if heart != 0:
    print('Number of ♥ is {}'.format(heart))
if diamond != 0:
    print('Number of ♦ is {}'.format(diamond))
if clover != 0:
    print('Number of ♣ is {}'.format(clover))
if spade != 0:
    print('Number of ♠ is {}'.format(spade))