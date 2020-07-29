# report.py
#
# Exercise 2.4
import sys
from pprint import pprint 
import csv
import fileparse

def read_portfolio(file):
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    prices= dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
    return prices

def make_report(portfolio,prices):
    report_list = []
    for share in portfolio:
        report_item = (share['name'],share['shares'],prices[share['name']],prices[share['name']]-share['price'])
        report_list.append(report_item)
    #pprint(report_list)
    return report_list

def print_report(reportdata):
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile,pricefile):        
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report_data(portfolio,prices)
    print_report(report)

portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')

