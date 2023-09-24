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




