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

            
