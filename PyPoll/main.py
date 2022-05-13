import os
import csv

# Define filepath
file = os.path.join('Resources', 'election_data.csv')

# Open csv
with open(file, 'r') as csvfile:
    # Define delimiter parameters
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    next(csvreader)
    # Create empty lists for 
    votes = []
    candidates = []
    # Append rows to outputs, change col 1 to integer values
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

# Total number of votes cast
total_votes = len(votes)

# Count for each candidate
charles_count = candidates.count("Charles Casper Stockham")
charles_percent = round((charles_count / total_votes) * 100)

diana_count = candidates.count("Diana DeGette")
diana_percent = round((diana_count / total_votes) * 100)

raymon_count = candidates.count("Raymon Anthony Doane")
raymon_percent = round((raymon_count / total_votes) * 100)

winner_list = [charles_count, diana_count, raymon_count]


if max(winner_list) == charles_count:
    winner = "Charles Casper Stockham"
elif max(winner_list) == diana_count:
    winner = "Diana DeGette"
elif max(winner_list) == raymon_count:
    winner = "Raymon Anthony Doane"


print(
f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {charles_percent}% ({charles_count})
Diana DeGette: {diana_percent}% ({diana_count})
Raymon Anthony Doane: {raymon_percent}% ({raymon_count})
-------------------------
Winner: {winner}
-------------------------
'''
)

#output_path = os.path.join("analysis", "output.txt")
with open ("analysis/output.txt", "w") as text_file:
    text_file.write(
        f'''
        Election Results
        -------------------------
        Total Votes: {total_votes}
        -------------------------
        Charles Casper Stockham: {charles_percent}% ({charles_count})
        Diana DeGette: {diana_percent}% ({diana_count})
        Raymon Anthony Doane: {raymon_percent}% ({raymon_count})
        -------------------------
        Winner: {winner}
        -------------------------
        '''
    )
