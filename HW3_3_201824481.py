def isTripleConsecutive(sentence):
    sentence = sentence.upper()
    for i in range(2, len(sentence)):
        if (ord(sentence[i]) - ord(sentence[i - 1])) == 1 and (ord(sentence[i - 1]) - ord(sentence[i - 2]) == 1):
            return True
        i += 1
    return False


def main():
    sentence = str(input('Enter a word: '))
    if isTripleConsecutive(sentence):
        print('{} contains three successive letters'.format(sentence))
    else:
        print('{} does not contains three successive letters'.format(sentence))
    print('in consecutive alphabetical order.')


main()