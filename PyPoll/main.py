import os
import csv

pyPollcsv = os.path.join("Resources", "election_data.csv")
#create the oupath for the text file
outpath = os.path.join("Resources", "election_data.txt")

#create variables
totalVotes = 0
charlesVote = 0
dianaVote = 0
raymondVote = 0
winner = 0
winPer = 0
winCan = 0

#open csv
with open(pyPollcsv) as file:
    csvreader = csv.reader(file, delimiter=",")
    next(csvreader) # no headers

    #loop to check the data 
    for row in csvreader:

            totalVotes +=1 
            candidateName = row[2]

            #calculate votes
            if candidateName == "Charles Casper Stockham":
                charlesVote += 1
            elif candidateName == "Diana DeGette":
                dianaVote +=1
            elif candidateName == "Raymond Anthony Doane":
                raymondVote += 1
           
    #calculate percentage
    charlesPer = (charlesVote/totalVotes)*100
    dianaPer = (dianaVote/totalVotes)*100
    raymondPer = (raymondVote/totalVotes)*100

    #determine winner
    if dianaVote > winner:
        winner = dianaVote
        winPer = dianaPer
        winCan = "Diana DeGette"
    elif charlesVote > winner:
        winner = charlesVote
        winPer = charlesPer
        winCan = "Charles Casper Stockham"
    elif raymondVote > winner:
        winner = raymondVote
        winPer = raymondPer
        winCan = "Raymond Anthony Doane"

#print function

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("------------------------------")
print("Charles Casper Stockham: " + "Per: " + str(charlesPer) + "Count: " + (str(charlesVote)))
print("Diana DeGette: " + "Per: " + str(dianaPer) + "Count: " + str(dianaVote))
print("Raymond Anthony Doane: " + "Per: " + str(raymondPer) + "Count: " + str(raymondVote))
print("----------------------------")
print("Winner: " + str(winCan))
print("------------------------------")

#output txtfile
with open(outpath, "w") as txtFile:
    txtFile.write("Election Results")
    txtFile.write("\n-------------------------")
    txtFile.write("\nTotal Votes: " + str(totalVotes))
    txtFile.write("\n------------------------------")
    txtFile.write("\nCharles Casper Stockham: " + "Per: " + str(charlesPer) + "Count: " + (str(charlesVote)))
    txtFile.write("\nDiana DeGette: " + "Per: " + str(dianaPer) + "Count: " + str(dianaVote))
    txtFile.write("\nRaymond Anthony Doane: " + "Per: " + str(raymondPer) + "Count: " + str(raymondVote))
    txtFile.write("\n----------------------------")
    txtFile.write("\nWinner: " + str(winCan))
    txtFile.write("\n------------------------------")