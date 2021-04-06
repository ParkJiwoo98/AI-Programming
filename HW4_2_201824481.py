while True:
    try:
        number = int(input('Enter an integer from 1 to 100: '))
        if number > 100 or number < 1:
            print('Your number was not between 1 and 100.')
        else:
            print('Your number is {}.'.format(number))
            break
    except ValueError:
        print('You did not enter an integer.')