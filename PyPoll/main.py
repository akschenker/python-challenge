import os
import csv

"""
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
"""

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	totalVotes = 0
	candidatesVotesDict = {}

	for row in csvreader:
		totalVotes += 1
		if row[2] in candidatesVotesDict:
			candidatesVotesDict[row[2]] += 1
		else:
			candidatesVotesDict[row[2]] = 1

	winningVotes = 0
	winnerName = ""
	for key, value in candidatesVotesDict.items():
		if value > winningVotes:
			winningVotes = value
			winnerName = key

textpath = os.path.join('PyPoll.txt')
with open(textpath, 'w', newline='') as textfile:
	def textprint(string):
		print(string)
		print(string, file=textfile)

	textprint("Election Results")
	textprint("-------------------------")
	textprint(f'Total Votes: {totalVotes}')
	textprint("-------------------------")
	for key, value in candidatesVotesDict.items():
		textprint(f'{key}: {round(value / totalVotes * 100, 3)}% ({value})')
	textprint("-------------------------")
	textprint(f'Winner: {winnerName}')
	textprint("-------------------------")
