import os
import csv

# To get data file
load_file = os.path.join(".", "Resources","election_data.csv")

# To set the path for new output file
output_file = os.path.join(".", "Analysis", "PyPoll_Analysis.txt")

# reset variable to 0
vote_count = 0

# To store Candidate list with their vote count resp. in dictionary
dict_candidate_list ={}

# To open file to read
with open(load_file) as data_file:
    csvreader = csv.reader(data_file, delimiter=',')
    
    # To get Header
    header = next(csvreader)
    
    # To read a file
    for row in csvreader:
        
        # To get Total vote count
        vote_count += 1
        
        # If candidate is not in dictionary then add candidate to it                
        if(row[2] not in dict_candidate_list):
            dict_candidate_list[row[2]] = 0
        
        # To change vote count to +1 for the same candidate resp. in dictionary
        dict_candidate_list[row[2]] += 1

# To get Winner who has max no. of votes
max_key = max(dict_candidate_list, key=dict_candidate_list.get)

# To concate output string with all result 
output = (
    "\nElection Results"+
    "\n----------------------------" +
    "\nTotal Votes: "+ str(vote_count) +
    f"\n----------------------------\n"
)

# To concate all candidates with number of votes and percentage resp.
for candidate in dict_candidate_list:
    output += f"{candidate}: {(dict_candidate_list[candidate]/vote_count)*100:.3f}% ({dict_candidate_list[candidate]})\n" 

output += "----------------------------\n"

# To concate Winner
output += "Winner: " + str(max_key) 
output += "\n----------------------------"

# To print Analysis
print(output)

with open(output_file, "w", newline='') as analysis_file:
    analysis_file.write(output)
    