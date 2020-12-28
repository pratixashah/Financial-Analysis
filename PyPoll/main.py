import os
import csv

# To get file path
file_path = os.path.join(".", "Resources","election_data.csv")

# To open file to read
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To get Header
    csvheader = next(csvreader)
    
    # reset variables to 0
    vote_count = 0
    
    def_candidate_list ={}
    
#     candidate_list = []
#     candidate_count_list = []

    # To get first row
    first_row = next(csvreader)
    
    # To get count from first row
    vote_count = 1
    
    # To get candidate Name from first row and set its count to 1
    def_candidate_list[first_row[2]] = 1

    # To read a file from next row 
    for row in csvreader:
        
        # To get Total vote count
        vote_count += 1
        
        # To get all Candidates and its vote count resp.
        if(row[2] in def_candidate_list):
            def_candidate_list[row[2]] += 1
        else:
            def_candidate_list[row[2]] = 1

# To print Analysis
output = (
    f"\nElection Analysis"
    f"\n---------------------------------------------"
    f"\nTotal Votes: {vote_count}"
    f"\n---------------------------------------------"
)

print(output)

# To print all candidates with total number of votes resp.
for candidate in def_candidate_list:
    print(f"{candidate}: {(def_candidate_list[candidate]/vote_count)*100:.3f}% ({def_candidate_list[candidate]})")

print("----------------------------")

# To print Winner who has max no. of votes
max_key = max(def_candidate_list, key=def_candidate_list.get)

print(f"Winner: {max_key}")
print("----------------------------")

output_file = os.path.join(".", "Analysis", "PyPoll_Analysis.txt")

with open(output_file, "w", newline='') as analysis_file:
    analysis_file.write(output)
    for candidate in def_candidate_list:
        analysis_file.write(f"\n{candidate}: {(def_candidate_list[candidate]/vote_count)*100:.3f}% ({def_candidate_list[candidate]})")

    analysis_file.write("\n----------------------------")

    analysis_file.write(f"\nWinner: {max_key}")
    analysis_file.write("\n----------------------------")
