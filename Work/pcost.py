# pcost.py
#
# Exercise 1.27
totalCost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        cost = int(row[1])*float(row[2])
        totalCost += cost
    print(f'Total Cost ${totalCost}')
