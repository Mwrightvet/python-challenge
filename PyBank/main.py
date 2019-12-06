import os
import csv

budget_data = os.path.join('budget_data.csv')

#total number of months included in the dataset
total_months = 0
#amount by month 
amount = 0 
#net total amount of "Profit/Losses" over the entire period
total_amount = 0
#average change by month 
change_Average_monthly = 0 
#change by month
change_by_month = 0
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
    print("Skipped header:", header)
    
    #remember that it will run until stopped so tell it that when there is nothing there to stop.
    #add if csv reader row is empty 
    # stop = open ("budget_data.csv")
    # for row in csv.reader(stop): 
    # if not row: 
    #     empty_rows += 1 
    #     continue
    # print row
    #iterate   
    for row in csvreader:
        #print (row[1]) #to view first column 0, to view second it's 1
        #add to total_month 
        total_months += 1
        total_amount += float(row[1])
        each_month_change = float(row[1]) - total_amount
    print("Financial Analysis")
    print("----------------------------------------")
    print("Total Months:" , total_months)
    print("Total Change:", average_change)
#net total amount of "Profit/Losses" over the entire period
    print("Total: $" , total_amount) 

#average of the changes in "Profit/Losses" over the entire period

#step 1 - loop through and make a list of changes, 
#Remember to tell it that if it's comparing the 2nd change from the top 
#step 2 - sum the list and divide by the len()

   # for row in csvreader: 
       # if amount != 0:
        #change_by_month = int(row[1]) - amount 
    #    change_Average_monthly += int(row[1]) - amount 

#greatest increase in profits (date and amount) over the entire period
#step 1 - loop through the list 
#step 2 - find the highest value using the if/else (built in check) sum and length**
        #if change_by_month < greatest_decrease:
         #   greatest_decrease_is = row[0]
          #  greatest_decrease = change_by_month
    #amount = int(row[1])

