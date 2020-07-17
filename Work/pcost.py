# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    totalCost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            try:
                row = line.split(',')
                cost = int(row[1])*float(row[2])
                totalCost += cost
               
            except ValueError:
                print('Value error occured')
        
    return totalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total Cost ${cost}')