# Retrieve list of candidates who recieved votes
# Retrieve number of votes cast for each candidate
# calculate total number of votes cast
# calculate percentage of votes cast for each candidate
# calculate winner of the election
import csv
import os

#cwd = os.getcwd()

#print("current working directory: {0}".format(cwd))
#assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#use the open statement to open the file as a text file
with open(file_to_load) as election_data:
    #To do: read and analyse the date here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read and print the header row
    headers = next(file_reader)
    print(headers)

    #print each row in the csv file
   # for row in file_reader:
     #   print(row[0])

