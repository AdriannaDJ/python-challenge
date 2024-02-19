# Goals: 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# print the analysis to the terminal and export a text file with the results.

import os
import csv

#empty lists
month = []
total_pl = []
dif_change = []

#open path to data
budgetpath = os.path.join('resources', 'budget_data.csv')

with open(budgetpath) as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',') #now we have a nested list
    
    #skip header row
    budget_header = next(budgetreader)

    #use for loop to create elements for lists - header has been skipped.
    for col in budgetreader:
        month.append(col[0])
        total_pl.append(int(col[1]))
            

    print("Financial Analysis\n\n------------------------------------------------\n")

    #total number of months
    total_month = str(len(month))
    print(f"Total Months: {total_month}")     # tested confirmed correct

    # Total$
    net_total_pl=sum(total_pl)
    print(f"Total: ${net_total_pl}") # tested confirmed correct

    #finding the average change
    for i in range(len(total_pl)-1):
        dif_change.append(total_pl [i+1] - total_pl [i])
        avg_change = sum(dif_change)/len(dif_change)
    #formatting 2 decimal places percentage by using ":.2f"
    print(f"Average Change: ${avg_change:.2f}")

    #Defining variables for max and min PLs
    max_pl = max(dif_change)
    min_pl = min(dif_change)

    #Finding index number for max and min PLs
    max_index=dif_change.index(max_pl)
    min_index=dif_change.index(min_pl)

    #Greatest increase/decrease in profits using max/min index numbers within month list
    print(f"Greatest Increase for profits: {month[max_index + 1]} ${max_pl}")
    print(f"Greatest Decrease for profits: {month[min_index + 1]} ${min_pl}")


    #Create new file for analysis results
output = os.path.join("analysis", "budget_results.txt")
with open(output, 'w') as budgetresults:

    writer = csv.writer(budgetresults, delimiter=',')

    #adding rows with analysis data
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------------------------------"])
    writer.writerow([f"Total Months: {total_month}"])
    writer.writerow([f"Total: ${net_total_pl}"])
    writer.writerow([f"Average Change: ${avg_change:.2f}"])
    writer.writerow([f"Greatest Increase for profits: {month[max_index + 1]} ${max_pl}"])
    writer.writerow([f"Greatest Decrease for profits: {month[min_index + 1]} ${min_pl}"])
