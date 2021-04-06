def getInputValue():
    interest = int(input('Enter annual rate of interest: '))
    payment = float(input('Enter monthly payment: '))
    beg = float(input('Enter beg. of month balance: '))
    return interest, payment, beg

def calculateValues(interest, payment, beg):
    interestPaid = beg * interest / 12 * 0.01
    reduction = payment - interestPaid
    endBalance = beg - reduction
    return interestPaid, reduction, endBalance

def printOut(interest, reduction, endBalance):
    print('Interest paid for the month: ${:,.2f}'.format(interest))
    print('Reduction of principal: ${:,.2f}'.format(reduction))
    print('End of month balance: ${:,.2f}'.format(endBalance))

a, b, c = getInputValue()
d, e, f = calculateValues(a, b, c)
printOut(d, e, f)