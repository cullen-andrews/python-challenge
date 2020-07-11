import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Stepping past the header row
    csv_header = next(csvreader)

    #Declaring lists for voter ID and candidate
    idList = []
    candidateList = []


    for row in csvreader:
        idList.append(row[0])
        candidateList.append(row[2])

#Now we have a list of candidate values for individual votes.
#Below I craft a list of unique candidate values.

#Declaring a list variable to store each unique value of candidate
unique_candidate = []



#This builds the list.
for vote in candidateList:
    if vote not in unique_candidate:
        unique_candidate.append(vote)

#List of lists of candidate and vote
candVoteList = []

#A list to pair candidates and vote counts
pair = []

for candidate in unique_candidate:
    
    pair = [candidate, candidateList.count(candidate)]

    candVoteList.append(pair)


#Counting votes
voteCount=len(idList)

#Determining the winner

#Declaring integer to track highest vote total among
#candidates as we iterate through candVoteList
maxVote = 0

for row in candVoteList:
    if row[1] > maxVote:
        maxVote = row[1]
        winner = row[0] #Stores winner name at end of loop
        winningVote = row[1]




#Creating and building a list of strings for printing
lineList = []

lineList.append("Election Results")
lineList.append("-------------------------")
lineList.append(f"Total Votes: {voteCount}")
lineList.append("-------------------------")

for row in candVoteList:
    lineList.append(f"{row[0]}: {round(row[1]/voteCount*100, 3)}% ({row[1]})")

lineList.append("-------------------------")
lineList.append(f"Winner: {winner}")
lineList.append("-------------------------")

#Creating text file and writing the results form lineList
textOut = open("analysis/results.txt", "w+")
for row in lineList:
    textOut.write(row + "\r")

for row in lineList:
    print(row)