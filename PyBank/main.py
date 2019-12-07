import os
import csv

budget_data = os.path.join('budget_data.csv')

#total number of months included in the dataset
total_months = 0
#net total amount of "Profit/Losses" over the entire period
total_amount = 0
#change by month
change_by_month = []
#average of the changes in "Profit/Losses" over the entire period
average_change = 0
#greatest increase in profits (date and amount) over the entire period
greatest_increase = 0 
#greatest decrease in profits (date and amount) over the entire period
greatest_decrease = 0 

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print("Financial Analysis")
    #Skipping the header 
    header = next(csvreader)
    #To see what I skipped . Confirm last command 
    #print("Skipped header:", header)

    #step 1 - Make a list of changes  

    csvreader = list(csvreader)
    
 
    for index, row in enumerate(csvreader): 
       # print(index, row)
        #print (row[1]) #to view first column 0, to view second it's 1
        #add to total_month 
        total_months += 1
        total_amount += float(row[1])
        total_change = total_amount / total_months
        
        # AVERAGE CHANGE CALCULATION
        # we need to keep track of the changes between two rows
        # skip first row for average change
        if (index != 0):
            each_month_change = float(row[1]) - int(csvreader[index - 1][1])
            change_by_month.append(each_month_change)
      
        #Remember to tell it that if it's comparing the 2nd change from the top 
        #step 2 - sum the list and divide by the len()
        #greatest increase in profits (date and amount) over the entire period
        #step 1 - loop through the list 
        #step 2 - find the highest value using the if/else (built in check) sum and length**
    average_change = sum(change_by_month) / len(change_by_month)
    greatest_increase = (max(change_by_month))
    greatest_decrease = min(change_by_month)
   

    print("----------------------------------------")
    print("Total Months:" , total_months)
    #print("Total Change:", total_change)
    print("Average Change $:", average_change)
    print("Greatest Increase $:", greatest_increase)
    print("Greatest Decrease $:", greatest_decrease)
    #net total amount of "Profit/Losses" over the entire period
    print("Total: $" , total_amount) 

output =(f"\nFinancial Analysis \n"
        f"------------------------- \n"
        f"Total Months: {total_months} \n"
        f"Average Change: ${average_change}  \n"
        f"Greatest Increase in Profits: ${greatest_increase}  \n"
        f"Greatest Decrease in Profits: ${greatest_decrease}  ")

with open(os.path.join('financial_analysis.txt'), "w") as txtfile:
    txtfile.write(output)