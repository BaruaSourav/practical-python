# report.py
#
# Exercise 2.4
import sys
from pprint import pprint 
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

def make_report(portfolio,prices):
    report_list = []
    for share in portfolio:
        report_item = (share['name'],share['shares'],prices[share['name']],prices[share['name']]-share['price'])
        report_list.append(report_item)
    #pprint(report_list)
    return report_list


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

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
        price_dollars = "${:.2f}".format(price)
        print(f'{name:>10s} {shares:>10d} {price_dollars:>10s} {change:>10.2f}')