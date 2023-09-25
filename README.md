# Python-Challenge

Overview of the Project: PyBank
    * Purpose : To analyze the financial records of your company.

# Data Given
    * Month & date, Profit/Losses

## Instructions

* The total number of months included in the dataset: Total Column 0, Set Varialbe = Total_Count

* The net total amount of "Profit/Losses" over the entire period: Total Column 1, Set Variable = Total_Profit_Loss

*The changes in "Profit/Losses" over the entire period, and then the average of those changes.

*The greatest increase in profits (date and amount) over the entire period. Variable = greatest_increase

*The greatest decrease in profits (date and amount) over the entire period. Variable = greatest_decrease

#Pseudo Code
import os
import csv

budget_csv = "/Users/manjushasethi/Downloads/Starter_Code 15/PyBank/Resources/budget_data.csv"

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total_month = 0
    month_of_change = []
    previous_profit_loss = 0
    profit_loss_change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999999999]
    total_profit_loss = 0

    for row in csvreader:
        total_month = total_month + 1
        profit_loss = int(row[1])
        total_profit_loss += profit_loss
        Profit_loss_change = profit_loss - previous_profit_loss
        previous_profit_loss = profit_loss
        profit_loss_change_list.append(Profit_loss_change)
        month_of_change.append(row[0])

        if Profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = Profit_loss_change

        if Profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Profit_loss_change

    Avg_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

output = (
    f"\nAnalysis\n"
    f"---------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total Profit/Loss: {total_profit_loss}\n"
    f"Average Profit/Loss Change: {Avg_change:.2f}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to the console
print(output)

# Write the output to a text file
output_file = "/Users/manjushasethi/Desktop/classwork/Python-Challenge/PyBank/Analysis"
with open(output_file, "w") as textfile:
    textfile.write(output)



Results:
Analysis
---------------------------
Total Months: 86
Total Profit/Loss: 22564198
Average Profit/Loss Change: 4448.13
Greatest Increase in Profit: Aug-16 ($1862002)
Greatest Decrease in Profit: Feb-14 ($-1825558)

##Pypoll Challenge

Purpose: To a small, rural town modernize its vote-counting process.

#Data Given
**Three columns: "Voter ID", "County", and "Candidate".

# Instructions
*The total number of votes cast

*A complete list of candidates who received votes

*The percentage of votes each candidate won

*The total number of votes each candidate won

*The winner of the election based on popular vote

#Psuedo Code
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

##Results

Election Results
---------------------
Total Votes = 369711
---------------------
Charles Casper Stockham: 23.049%: (85213)
Diana DeGette: 73.812%: (272892)
Raymon Anthony Doane: 3.139%: (11606)
---------------------
Winner: = Diana DeGette
---------------------