def reverseState():
    state = str(input('Enter a state: '))
    if state == 'End':
        return 0
    else:
        reverseState()
        print(state)

reverseState()