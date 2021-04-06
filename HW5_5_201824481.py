import random


class Contestant:
    name = ''
    score = 0

    def __init__(self, name):
        self.name = name
        self.score = 0

    def upScore(self):
        self.score += 1

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def __str__(self):
        return self.name + ': ' + str(self.score)


class Human(Contestant):
    choice = ''

    def selection(self):
        self.choice = str(input('{}, enter your choice: '.format(self.name)))

    def getSelection(self):
        return self.choice


class Computer(Contestant):
    choice = ''

    def selection(self):
        self.choice = random.choice(['rock', 'scissors', 'paper'])
        print('{} chooses {}'.format(self.name, self.choice))

    def getSelection(self):
        return self.choice


humanName = str(input('Enter name of human: '))
computerName = str(input('Enter name of computer: '))

human = Human(humanName)
computer = Computer(computerName)
print()

for i in range(0, 3):
    human.selection()
    computer.selection()

    if human.getSelection() == 'rock':
        if computer.getSelection() == 'scissors':
            human.upScore()
        elif computer.getSelection() == 'paper':
            computer.upScore()

    elif human.getSelection() == 'scissors':
        if computer.getSelection() == 'rock':
            computer.upScore()
        elif computer.getSelection() == 'paper':
            human.upScore()

    else:
        if computer.getSelection() == 'rock':
            human.upScore()
        elif computer.getSelection() == 'scissors':
            computer.upScore()

    print(human.__str__(), computer.__str__())
    print()

if human.getScore() > computer.getScore():
    print('{} WINS'.format(humanName.upper()))
elif human.getScore() < computer.getScore():
    print('{} WINS'.format(computerName.upper()))
else:
    print('TIE')