import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    rowcount = 0
    net_total_amount = 0
    greatest__increase_profit_date = 0
    greatest__increase_profit = 0
    
    greatest__decrease_profit_date = 0
    greatest__decrease_profit = 0
    
    first_row_profit = 0
    profit_change = 0
    total_profit_change = 0
    
    csv_header = next(csvreader)
    
    first_row = next(csvreader)

    rowcount += 1
    net_total_amount += int(first_row[1])
    previous_profit = int(first_row[1])  
    
    print("Financial Analysis")
    print("---------------------------------------------")