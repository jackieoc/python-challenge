
import csv

#specify the file path
file_path = "Resources/budget_data.csv"

#create two lists to store data in csv
date = []
profit_loss = []

#open cvs file
with open(file_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])

#zip the two lists
df = list(zip(date, profit_loss))

#financial analysis
title = "Financial Analysis"
print(title + "\n" + "----------------------------")   

#total number of months
total_month = len(df)
print(f"Total Months: {total_month}")

#total amount of "Profit/Losses"
total = 0

#calculate total
for i in range(len(df)):
   value = df[i][1]
   total += int(value)
print(f"Total: ${total}")

#create list for changes in "Profit/Losses"
change = [0]

#loop through to calculate the changes
for i in range(1, len(df)):
    value1 = int(df[i-1][1])
    value2 = int(df[i][1])
    diff = value2 - value1
    change.append(diff)

#make the change list into int
change = list(map(int, change))

#add date, profit_loss, and change into a dictionary
df = dict({'date': date, 
           'profit_loss': profit_loss,
           'change': change})

#create a variable, sum_diff, for the sum of changes
sum_diff = 0
for i in range(1, len(df['change'])):
    sum_diff += df['change'][i]
#calculate the average changes
avg_change = round(sum_diff / (len(df['change'])-1), 2)
print(f"Average Change: ${avg_change}")

#create variables for the greatest increase and date
max = df['change'][0]
greatest_month = df['date'][0]
for i in range(1, len(df['date'])):
    # if the df['change'][i] is greater than the current max value
    if df['change'][i] > max:
        max = df['change'][i]
        greatest_month = df['date'][i]

print(f"Greatest Increase in Profits: {greatest_month} (${max})")

#create variables for greatest decrease
min = df['change'][0]
lowest_month = df['date'][0]
for i in range(1, len(df['date'])):
    # if the df['change'][i] is less than current min value
    if df['change'][i] < min:
        # then make min = df['change'][i] and lowest_month = df['date'][i]
        min = df['change'][i]
        lowest_month = df['date'][i]

print(f"Greatest Decrease in Profits: {lowest_month} (${min})")

output_path = "analysis/PyBank_result.txt"
with open(output_path, "w") as file:
   file.write(f"Financial Analysis" + '\n')
   file.write("----------------------------" + '\n')
   file.write(f"Total Month: {total_month}"+ '\n')
   file.write(f"Total: ${total}"+ '\n')
   file.write(f"Average Change: ${avg_change}"+ '\n')
   file.write(f"Greatest Increase in Profits: {max} (${greatest_month})"+ '\n')
   file.write(f"Greatest Decrease in Profits: {min} (${lowest_month})")
