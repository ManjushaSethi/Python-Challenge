import os
import csv

# File import
#election_csv= os.path.join("Resources", "election_data.csv")
#Analysis_output = os.path.join("analysis", "election_analysis.txt") 
election_csv = "/Users/manjushasethi/Desktop/classwork/Python-Challenge/Pypoll/Resources/Starter_Code 16/PyPoll/Resources/election_data.csv"
Analysis_Output = "/Users/manjushasethi/Desktop/classwork/Python-Challenge/Pypoll/Analysis"
# Open csv reader
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)
    total_votes = 0
    candidate_votes = {}
    candidate_options = []
    winning_candidate = ""
    winning_votes = 0

# Total Votes
    for row in csvreader:
        total_votes = total_votes + 1
    
    #Candidate nmae and votes
        candidate_name = str(row[2])
# Find different Candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
# Print result    
   
with open(Analysis_Output, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes = {total_votes}\n"
        f"---------------------\n"
        )
    print(election_results)

    txt_file.write(election_results)


    #Winning Candidate and corresponding total votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)*100

     # Winner
        if (votes > winning_votes):
            winning_votes = votes
            winning_candidate = candidate
    # print results
        voter_output = (f"{candidate}: {vote_percentage:.3f}%: ({votes})\n")
        print(voter_output)
    
        txt_file.write(voter_output)

   # print winning candidate

    winning_candidate_summary = (
    f"---------------------\n"
    f"Winner: = {winning_candidate}\n"
    f"---------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

