# Let's import the packages needed
# os will allow us to create file paths accross operating systems
# csv is for reading CSV files
import os
import csv

# Let's begin by setting the csv path
csv_path_PyPoll = os.path.join(".","Resources","election_data.csv")

with open(csv_path_PyPoll) as csv_file_PyPoll:

    # CSV reader specifies delimiter and variable
    csv_reader = csv.reader(csv_file_PyPoll, delimiter = ",")

    # Convert CSV reader to a list 
    data_list = list(csv.reader(csv_file_PyPoll, delimiter = ","))
    
    # Initial variables
    total_votes = len(data_list) - 1
    candidate_1_votes = 0
    candidate_2_votes = 0
    candidate_3_votes = 0

    for row in range(1, total_votes):
        if data_list[row][2] == "Charles Casper Stockham":
            candidate_1_votes = candidate_1_votes + 1
        elif data_list[row][2] == "Diana DeGette":
            candidate_2_votes = candidate_2_votes + 1
        elif data_list[row][2] == "Raymon Anthony Doane":
            candidate_3_votes = candidate_3_votes + 1

    candidate_1_percent = candidate_1_votes/(len(data_list) - 1)*100
    candidate_2_percent = candidate_2_votes/(len(data_list) - 1)*100
    candidate_3_percent = candidate_3_votes/(len(data_list) - 1)*100

    # Create a dictionary
    Candidates = {"Candidate 1": ["Charles Casper Stockham",candidate_1_votes, candidate_1_percent],
                  "Candidate 2": ["Diana Degette", candidate_2_votes, candidate_2_percent],
                  "Candidate 3": ["Raymon Anthony Doane",candidate_3_votes, candidate_3_percent]}

    # Find the winner
    candidates_votes = [Candidates["Candidate 1"],
                        Candidates["Candidate 2"],
                        Candidates["Candidate 3"]]
    
    winner = ["name","number of voter"]

    greatest_vote = 0
    for i in range(0,len(candidates_votes)):
        if candidates_votes[i][1] > greatest_vote:
            greatest_vote = candidates_votes[i][1]
            winner[0] = candidates_votes[i][0]
            winner[1] = candidates_votes[i][1]


    print(f"Election Results")
    print(f"--------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------")
    print(f"{Candidates['Candidate 1'][0]}: {round(candidate_1_percent,3)}% ({candidate_1_votes})")
    print(f"{Candidates['Candidate 2'][0]}: {round(candidate_2_percent,3)}% ({candidate_2_votes})")
    print(f"{Candidates['Candidate 3'][0]}: {round(candidate_3_percent,3)}% ({candidate_3_votes})")

    print(f"--------------------")
    print(f"Winner : {winner[0]}")


