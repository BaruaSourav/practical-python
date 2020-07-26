# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    totalCost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for rowno, row in enumerate(f, start =1):
            try:
                portfolioInstance = row.split(',')
                cost = int(portfolioInstance[1])*float(portfolioInstance[2])
                totalCost += cost
               
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        
    return totalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)
print(f'Total Cost ${cost}')