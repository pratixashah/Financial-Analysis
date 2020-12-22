import os
import csv

# To get file path
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# To open file to read
with open(csvpath , 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # reset variables to 0
    
    month_count = 0
    net_total_amount = 0
    
    greatest__increase_profit_date = 0
    greatest__increase_profit = 0
    
    greatest__decrease_profit_date = 0
    greatest__decrease_profit = 0
    
    first_row_profit = 0
    profit_change = 0
    total_profit_change = 0
    
    # To get Header
    csv_header = next(csvreader)
    
    # To get first row
    first_row = next(csvreader)

    # To get count from first row
    month_count += 1
    net_total_amount += int(first_row[1])
    previous_profit = int(first_row[1])  
    
    # To read file from next row
    for row in csvreader:
        
        # To get Month count, Total Amount 
        month_count += 1
        net_total_amount += int(row[1])
        
        # To get Profit Change from currunt and last row
        profit_change = int(row[1]) - previous_profit
        
        # To get Total Profit Change
        total_profit_change += profit_change
        previous_profit = int(row[1])
            
        # To get Greatest Increase in Profit with its Month resp.
        if(profit_change > greatest__increase_profit):
            greatest__increase_profit_date = row[0]
            greatest__increase_profit = profit_change
        
        # To get Greatest Decrease in Profit with its Month resp.
        if(profit_change < greatest__decrease_profit):
            greatest__decrease_profit_date = row[0]
            greatest__decrease_profit = profit_change

    # To print Analysis
    print("\nFinancial Analysis")
    print("---------------------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total : ${net_total_amount}")
    print(f"Average Change : ${round(float(total_profit_change/(month_count-1)),2)}")
    print(f"Greatest Increase in Profits in {greatest__increase_profit_date} (${greatest__increase_profit})")
    print(f"Greatest Decrease in Profits in {greatest__decrease_profit_date} (${greatest__decrease_profit})")
    
    # To Create dictionary with calculated data   
    myDictionary = {
        "Total Months": month_count,
        "Total": net_total_amount,
        "Average Change": round(float(total_profit_change/(month_count-1)),2),
        "Greatest Increase in Profits" : [greatest__increase_profit_date,greatest__increase_profit],
        "Greatest Decrease in Profits" : [greatest__decrease_profit_date,greatest__decrease_profit]
    }

    # To write result into file
    # To set the path from new file
    output_file = os.path.join(".", "Analysis", "PyBank_Analysis.csv")

    with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)

        writer.writerow(["Financial Analysis"])
        writer.writerow(["---------------------------------------------"])
        writer.writerow([f"Total Months: {myDictionary['Total Months']}"])
        writer.writerow([f"Total: ${myDictionary['Total']}"])
        writer.writerow([f"Average Change: ${myDictionary['Average Change']}"])
        writer.writerow([f"Greatest Increase in Profits in {myDictionary['Greatest Increase in Profits'][0]} (${myDictionary['Greatest Increase in Profits'][1]})"])
        writer.writerow([f"Greatest Decrease in Profits in {myDictionary['Greatest Decrease in Profits'][0]} (${myDictionary['Greatest Decrease in Profits'][1]})"])