futureValue = float(input('Enter future value: '))
interestRate = 1 + float(input('Enter interest rate (as %): ')) / 100
years = int(input('Enter number of years: '))
i = 0
rate = 1
for i in range(0, years):
    rate *= interestRate
presentValue = futureValue / rate
print('Present value: ${:,.2f}'.format(presentValue))