# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(file):
    portfolio=[]
    with open(file) as f:
        rows = csv.reader(f)
        header = next(rows)
        for item in rows:
            rowDictionary = {}
            rowDictionary['name'] = item[0]
            rowDictionary['shares'] = int(item[1])
            rowDictionary['price'] = float(item[2]) 
            portfolio.append(rowDictionary)
    return portfolio

def read_prices(filename):
    prices= {}
    f = open(filename,'r')
    rows= csv.reader(f)
    for row in rows:
        #print(row[0],row[1])
        try:
            prices[row[0]] = float(row[1])
        except:
            print('Bad row')
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

totalCost = 0.0 
for share in portfolio:
    totalCost += share['shares']*share['price']

sumOfPresentValue = 0.0 
for share in portfolio:
    sumOfPresentValue += share['shares']*prices[share['name']]

print("Total buying cost ", totalCost)
print("Current price: ", sumOfPresentValue)
if (totalCost<sumOfPresentValue):
    print("Profit/Gain: ", sumOfPresentValue-totalCost)
else:
    print("Loss : ",totalCost-sumOfPresentValue)