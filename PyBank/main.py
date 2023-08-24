# Let's import the packages needed
# os will allow us to create file paths accross operating systems
# csv is for reading CSV files

import os
import csv

# Let's begin by setting the csv path
csv_path_PyBank = os.path.join(".","Resources","budget_data.csv")

with open(csv_path_PyBank) as csv_file_PyBank:

    # CSV reader specifies delimiter and variable
    csv_reader = csv.reader(csv_file_PyBank, delimiter = ",")

    # Convert CSV reader to a list 
    data_list = list(csv.reader(csv_file_PyBank, delimiter = ","))

    # Initial variables
    number_of_months = 0
    total = 0 
    greatest_profit_increase = 0
    greatest_profit_increase_index = 0
    greatest_profit_decrease = 0
    greatest_profit_decrease_index = 0

    # Initial array
    change = []
    
    # For loop to compute the total $
    for row in range(1,len(data_list)):
        
        #print(data_list[row][1])
        
        total = total + float(data_list[row][1])

    # For loop to compute the other statistics
    for row in range(1,len(data_list) - 1):

        # Compute the array with all the monthly changes
        difference = float(data_list[row + 1][1]) - float(data_list[row][1])
        change.append(difference)

        # Compute greatest profit increase
        if (float(data_list[row + 1][1]) - float(data_list[row][1]) > greatest_profit_increase):
            greatest_profit_increase = float(data_list[row + 1][1]) - float(data_list[row][1])
            greatest_profit_increase_index = row + 1

        # Compute greatest profit decrease
        if (float(data_list[row + 1][1]) - float(data_list[row][1]) < greatest_profit_decrease):
            greatest_profit_decrease = float(data_list[row + 1][1]) - float(data_list[row][1])
            greatest_profit_decrease_index = row + 1

    average_change = sum(change)/(len(data_list) - 1)

    print(f"Financial Analysis")
    print(f"- - - - - - - - - - - ")
    print(f"Total Months: {len(data_list) - 1}")
    print(f"Total: $ {total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {data_list[greatest_profit_increase_index][0]} (${greatest_profit_increase})")
    print(f"Greatest Decrease in Profits: {data_list[greatest_profit_decrease_index][0]} (${greatest_profit_decrease})")