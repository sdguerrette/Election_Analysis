# Retrieve list of candidates who recieved votes
# Retrieve number of votes cast for each candidate
# calculate total number of votes cast
# calculate percentage of votes cast for each candidate
# calculate winner of the election
import csv
import os
from tkinter import N

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize variable to count total votes
total_votes = 0

#create a list to hold all of the candidate names
candidate_options = []
#create an empty dictionary to hold each candidate and their total votes
candidate_votes = {}
#winning candidate and winnig vote count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#use the open statement to open the file as a text file
with open(file_to_load) as election_data:
    #To do: read and analyse the date here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
      total_votes += 1
      #print the candidate name from each row
      candidate_name = row[2]
      #check if candidate name is in the candidate_options list, if not, append it to the list
      if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        #begin tracking each candidates vote count
        candidate_votes[candidate_name] = 0
      
      #increment the each candidates vote by 1 each time they appear
      candidate_votes[candidate_name] += 1  
#save results to a text file
with open(file_to_save, "w") as txt_file:

  election_results = (
  f'\n'
  f'Election Results\n'
  f'----------------------\n'
  f'Total Votes: {total_votes:,}\n'
  f'----------------------\n'
)
  print(election_results, end="")
  txt_file.write(election_results)

    #itereate thru the candidate list
  for candidate_name in candidate_options:
      #retrieve amount of votes cast for each candidate
      votes = candidate_votes[candidate_name]
      #calculate the vote percentage of each candidate
      vote_percentage = float(votes)/float(total_votes) * 100
      
      #print out each candidate's name, vote count, and percentage votes to the terminal
      candidate_results = (f'{candidate_name} received {vote_percentage:.1f}% of the vote with {votes:,} votes.\n')
      print(candidate_results)
      txt_file.write(candidate_results)
      #determine wining vote count and candidate
      ##determine if a candidates votes is greater than the winning count
      if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    #print the winning candidate and their stats
  winning_candidate_summary = (
    f"----------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"----------------------------------------------\n")
      
  print(winning_candidate_summary)
  txt_file.write(winning_candidate_summary)



