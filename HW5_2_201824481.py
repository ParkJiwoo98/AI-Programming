import Fraction

numerator = int(input('Enter numerator of fraction: '))
denominator = int(input('Enter denominator of fraction: '))
GCD = Fraction.Fraction.GCD(numerator, denominator)
print('Reduction to lowest terms: {0}/{1}'.format(numerator//GCD, denominator//GCD))