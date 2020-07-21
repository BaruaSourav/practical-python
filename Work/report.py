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

            
