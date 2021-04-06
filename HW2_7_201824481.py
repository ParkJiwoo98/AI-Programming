number = int(input('How many people? '))
person = []
i = 0
while i < number:
    print('Person', i + 1)
    firstName = str(input('Enter first name: '))
    lastName = str(input('Enter last name: '))
    current = int(input('Enter current salary: '))
    newSalary = 0
    if current < 40000:
        newSalary = current + current * 0.05
    else:
        newSalary = current + 2000 + (current - 40000) * 0.02
    person.append([firstName, lastName, current, newSalary])
    i += 1
print('{0:^6}{1:<14}{2:<14}{3:<19}{4:<19}'.format('Index', 'First Name', 'Last Name',
                                                  'Current Salary', 'New Salary'))
i = 0
while i < number:
    print('{0:^6}{1:<14}{2:<14}{3:<19,.2f}{4:<19,.2f}'.format(i, person[i][0], person[i][1],
                                                              person[i][2], person[i][3]))
    i += 1