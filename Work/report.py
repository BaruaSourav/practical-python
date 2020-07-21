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
            holding = (item[0],int(item[1]),float(item[2]))
            portfolio.append(holding)
    return portfolio

            
