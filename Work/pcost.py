# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    totalCost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            try:
                row = line.split(',')
                cost = int(row[1])*float(row[2])
                totalCost += cost
            print(f'Total Cost ${totalCost}')
            except ValueError:
                print('Value error occured')
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)