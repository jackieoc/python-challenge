import os
import csv


#list to store data
date = []
profit_losses = []


# with open (udemy_csv, encoding='utf-8') as csvfile
with open('./Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  
    #find number of months
    for row, value in enumerate(csvreader, start=1):
        print(row, value)




