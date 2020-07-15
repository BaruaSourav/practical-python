# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

first_year_payment = 1000.0

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= 1 and month <= 12:
        principal = principal - first_year_payment
        total_paid = total_paid + first_year_payment

    print("Month "+ str(month))
    print("Total Paid : " + str(total_paid))
    print("Principal : " + str(principal))
    print("--------------------------------")
    
print('Total paid :' + str(round(total_paid, 2)))
print('Months :' + str(month))



