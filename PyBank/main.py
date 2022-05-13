import os
import csv

# Define filepath
file = os.path.join('Resources', 'budget_data.csv')

# Open csv
with open(file, 'r') as csvfile:
    # Define delimiter parameters
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    next(csvreader)
    # Create empty lists for total months and profit/loss outputs
    months = []
    pnl = []
    pnl_changes = []
    # Append rows to outputs, change col 1 to integer values
    for row in csvreader:
        months.append(row[0])
        pnl.append(int(row[1]))
    # Create list of changes from period to period
    for entry in range(1, len(months)):
        changes = pnl[entry] - pnl[entry - 1]
        pnl_changes.append(changes)

# Length of months is length of total_months
months_length = len(months)

# Length of pnl
pnl_length = len(pnl_changes)

# Total profit/loss is sum of pnl
total_pnl = sum(pnl)

total_pnl_changes = sum(pnl_changes)

# Average profit/loss is average of pnl, round to 2 decimals
average_pnl = round(total_pnl_changes / (pnl_length), 2)

# Max pnl, index of max pnl, date using index of max pnl
max_pnl = max(pnl_changes)
max_pnl_index = pnl_changes.index(max_pnl)
max_pnl_date = months[max_pnl_index + 1]

# Min pnl, index of min pnl, date using index of min pnl
min_pnl = min(pnl_changes)
min_pnl_index = pnl_changes.index(min_pnl)
min_pnl_date = months[min_pnl_index+ 1]

# Output

print(
    f'''
Financial Analysis
----------------------------
Total Months: {months_length}
Total: ${total_pnl}
Average Change: ${average_pnl}
Greatest Increase in Profits: {max_pnl_date} (${max_pnl})
Greatest Decrease in Profits: {min_pnl_date} (${min_pnl})
'''
)

with open("analysis/output.txt", "w") as text_file:
    text_file.write(
        f'''
        Financial Analysis
        ----------------------------
        Total Months: {months_length}
        Total: ${total_pnl}
        Average Change: ${average_pnl}
        Greatest Increase in Profits: {max_pnl_date} (${max_pnl})
        Greatest Decrease in Profits: {min_pnl_date} (${min_pnl})
        '''
    )
