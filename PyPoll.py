#The Data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recived votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote. 

# Import the datetime class from the datetime module.
from calendar import c
import datetime
# Use the now() attribute on the datetime class to get the present time.
now=datetime.datetime.now()
# Print the present time.
print("The time right now is", now) 

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save=os.path.join("Resources", "analysis")

# Initialize a total vote counter.
total_votes=0

# Candidate options and candidate votes.
candidate_options=[]
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Read the header row.
    headers=next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name for each row.
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name]=0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes=candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100
    # Print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n")

    # Determine winning vote count and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
# Print out the winning candidate, vote count, and percentage to votes the the terminal.
winning_candidate_summary=(
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")

print(winning_candidate_summary)


































