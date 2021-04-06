def displaySequenceOfNumbers(m, n):
    if m > n:
        return 0
    else:
        print(m)
        return displaySequenceOfNumbers(m + 1, n)