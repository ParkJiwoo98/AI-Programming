def main():
    letter = str(input('Enter a letter to count: '))
    sentence = str(input('Enter a sentence: '))
    print('Count:', countLetter(letter, sentence))
def countLetter(l, s):
    i = 0
    count = 0
    while i < len(s):
        if l == s[i]:
            count += 1
        i += 1
    return count
main()