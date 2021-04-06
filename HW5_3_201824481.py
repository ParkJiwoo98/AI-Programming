import Fraction

number = str(input('Enter a positive decimal number less than 1: '))
index = number.find('.')
numerator = int(number[index + 1:])
denominator = 10 ** (len(number) - index - 1)
GCD = Fraction.Fraction.GCD(denominator, numerator)
print('Converted to fraction: {0}/{1}'.format(numerator//GCD, denominator//GCD))