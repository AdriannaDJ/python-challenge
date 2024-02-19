# Goals: 
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# print the analysis to the terminal and export a text file with the results.

import os
import csv

#empty lists
ballot_id=[]
candidates_name=[]
counts={}

#open path to data
electionpath = os.path.join('resources', 'election_data.csv')

with open(electionpath) as electionfile:
    electionreader = csv.reader(electionfile, delimiter=',') #now we have a nested list
    
    #skip header row
    election_header = next(electionreader)

    #use for loop to create elements for lists - header has been skipped.
    for col in electionreader:
        ballot_id.append(col[0])
        candidates_name.append(col[2])

    #print header
    print(f"Election Results\n\n---------------------------\n")

    #total number of votes cast
    total_votes = len(ballot_id)
    print(f"Total Votes: {total_votes}\n\n---------------------------\n")

    #list of candidates name and total votes placed into dictionary
    for i in candidates_name:
        counts[i] = counts.get(i, 0) + 1

    # defining the key, values in counts (dictionary). Calculate percentages.
    for name, count in counts.items():
        percentage_votes = count/total_votes * 100
        print(f"{name}: {percentage_votes:.2f}% ({count})")
    
    #print Winner based on max value in counts (dictionary).
    print(f"\n\n---------------------------\n")
    print(f"Winner: {max(counts, key=counts.get)}\n\n---------------------------\n")

output = os.path.join("analysis", "election_results.txt")
with open(output, 'w') as electionresults:

    writer = csv.writer(electionresults, delimiter=',')

    writer.writerow([f"Election Results\n---------------------------"])
    writer.writerow([f"Total Votes: {total_votes}\n---------------------------"])

    for name, count in counts.items():
        percentage_votes= count/total_votes * 100
        writer.writerow([f"{name}: {percentage_votes:.2f}% ({count})"])
    
    writer.writerow([f"---------------------------"])
    writer.writerow([f"Winner: {max(counts, key=counts.get)}\n---------------------------"])