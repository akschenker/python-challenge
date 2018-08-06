import os
import csv

"""
The total number of months included in the dataset
The total net amount of "Profit/Losses" over the entire period
The average change in "Profit/Losses" between months over the entire period
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in losses (date and amount) over the entire period
"""

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	monthTotal = 0
	totalProfit = 0
	maxProfit = 0
	maxProfitDate = ""
	minProfit = 0
	minProfitDate = ""
	revenueList = []

	for row in csvreader:
		monthTotal += 1
		revenue = int(row[1])
		revenueList.append(revenue)

		totalProfit += revenue
		if revenue > maxProfit:
			maxProfit = revenue
			maxProfitDate = row[0]
		elif revenue < minProfit:
			minProfit = revenue
			minProfitDate = row[0]

changeList = []
for i in range(len(revenueList)):
	if i > 0:
		changeList.append(revenueList[i] - revenueList[i - 1])

averageChange = sum(changeList) / len(changeList)



def textprint(string, textfile):
	print(string)
	print(string, file=textfile)

outputPath = os.path.join('PyBank.txt')

with open(outputPath, 'w', newline='') as txtfile:
	textprint("Financial Analysis", txtfile)
	textprint("-----------------------------", txtfile)
	textprint(f'Total Months: {monthTotal}', txtfile)
	textprint(f'Total: ${totalProfit}', txtfile)
	textprint(f'Average Change: {averageChange}', txtfile)
	textprint(f'Greatest Increase in Profits: {maxProfitDate} (${maxProfit})', txtfile)
	textprint(f'Greatest Decrease in Profits: {minProfitDate} (${minProfit})', txtfile)

