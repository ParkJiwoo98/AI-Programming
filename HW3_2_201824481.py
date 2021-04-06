def factorial(n):
    i = 1
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


def isPrime(n):
    if n <= 1:
        return False
    value = factorial(n - 1) + 1
    if value % n == 0:
        return True
    return False


startNumber = int(input('Enter the first integer greater than 1: '))
endNumber = int(input('Enter the last integer greater than {}: '.format(startNumber)))
primeNumber = []
print('Prime number')
for i in range(startNumber, endNumber + 1):
    if isPrime(i):
        primeNumber.append(i)

for i in range(1, len(primeNumber)):
    if i % 10 != 0:
        print('{0:4}, '.format(primeNumber[i - 1]), end='')
    else:
        print('{0:4}, '.format(primeNumber[i - 1]))
print('{0:4}'.format(primeNumber[len(primeNumber) - 1]))