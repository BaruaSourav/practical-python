# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename,select = None,types = None,has_headers = True,delimiter = ',',silence_erros = False ):
    '''
    Generic function to parse csv files
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)
        headers = next(rows) if has_headers else []
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for rowno, row in enumerate(rows,1):
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_erros:
                        print(f"Row {rowno}: error while reading the row {row} for {e}")

            #make dict or tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records

