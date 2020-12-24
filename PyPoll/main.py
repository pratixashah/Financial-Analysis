import os
import csv

csvpath = os.path.join(".", "Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvreader)
    
    vote_count = 0
    
    def_candidate_list ={}
    
    candidate_list = []
    candidate_count_list = []

    first_row = next(csvreader)
    vote_count = 1
    def_candidate_list[first_row[2]] = 1

    for row in csvreader:
        vote_count += 1
        
        if(row[2] in def_candidate_list):
            def_candidate_list[row[2]] += 1
        else:
            def_candidate_list[row[2]] = 1