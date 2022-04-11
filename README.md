# Election Analysis Challenge
## Election Audit Overview
This project was underataken to determine the the winning candidate for Colorado's 1st conggressional disctrict. To determine the winning candidate, the election data was extracted from a CSV file provided by the distrcit containing the following information: ballot I.D., county of vote origin, and selected candidate. This data was parsed using a Python script to aggregate the total number of votes, as well as number and percentage of votes for each county and candidate. The results can be found below. 
## Election Audit Results
  - Total Votes Cast: 369,711
  - County Summary:
     - Jefferson County:  10.5% of the vote with 38,855 votes cast.
     - Denver County:     82.8% of the vote with 306,055 votes cast.
     - Arapahoe County:   3.1% of the vote with 11,606 votes cast.
  - Largest County Turnout: Denver
  - Candidate Summary
    - Charles Casper Stockholm received 23.0% of the vote with 85,213 votes received.
    - Diana DeGette received 73.8% of the vote with 272,892 votes received.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes received.
  - Winning Candidate: Diana DaGette won the election by receiving 73.8% of the vote with 272,892 votes received.
## Election Audit Summary
With the success of the script, we believe that the State of Colorado Election Commission would benifit by adopting and generalizing its use to be applied to any type of elecition within the state. The believe making the following changes would be in the best interest of the State.
1. A section of code would be inserted into the beginning of the program that pulls information from the header of the accompanying CSV file. The focus of this code would be to gather the region type data for the election. In the instance of the congressional election, the region type would be "county." Other such types could be municipality, congressional district, or state.
2. Once extracted from the CSV file, the region type would be assigned to a variable that would then be referenced throughout the rest of the code. This would ensure that the proper type is displayed to the terminal, as well as the text file that is created when the code is run. 
We believe making these changes would allow the Election Commison to confidently apply this program to a variety of elections throughout the entire state, while ensure the results are displayed in and accurate, clean, and readable manner. 
  

