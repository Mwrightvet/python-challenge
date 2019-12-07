import csv
import os

total_votes = 0
candidate_name = []
total_vote_each = {}
winner = ''
winner_count = 0
percentage_votes = []

csvpath = os.path.join('..', 'Pypoll', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header in analysis
    csv_header = next(csvreader)

    for row in csvreader:
        #Find the total number of votes  
        total_votes += 1
        #Identify the candidates
        candidate = row[2]
        # Remember to isolate the candidates only when they match 
        # It needs to keep track of the candidates as it's looping
        if candidate not in candidate_name:
        # Add to the list of candidates
            candidate_name.append(candidate)
            #add up the votes for each candidate
            total_vote_each[candidate] = 0
        #we need to keep track of the votes by candidate to know the total for each
        #this finds the total for each 
        total_vote_each[candidate] += 1

    for candidate in total_vote_each:
        votes = total_vote_each.get(candidate)
        percentage = (float(votes)/float(total_votes)) * 100
        percentage = round(percentage, 3)
        percentage_votes.append(percentage)
        
        #Identify the winner as the one with the highest count 
        #Step 1: have it see which total votes are highest
        #Step 2: have it identify the winning candidate 
        if (votes > winner_count):
            winner_count = votes
            winner = candidate

    khan_percent = str(float(percentage_votes[0])) + "% (" + str((total_vote_each['Khan'])) + ")"
    correy_percent = str(float(percentage_votes[1])) + "% (" + str((total_vote_each['Correy'])) + ")"
    li_percent = str(float(percentage_votes[2])) + "% (" + str((total_vote_each['Li'])) + ")"
    otooley_percent = str(float(percentage_votes[3])) + "% (" + str((total_vote_each["O'Tooley"])) + ")"
    

    
    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(total_votes))
    print("----------------")
    
    #Reference back to the previous calculations 
    #Remember to test each and check the formatting 
    print("Khan:" , khan_percent)
    print("Correy:" , correy_percent)
    print("Li:" , li_percent)
    print("O'Tooley:" , otooley_percent)

    print("-----------------")
    print("Winner: " + winner)
    print("------------------")
    print("Congratulations to", winner,"!")

output_path = os.path.join("election_results.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write(f"---------------------")
    txtfile.write(f"Khan: {khan_percent}")
    txtfile.write(f"Correy:{correy_percent}")
    txtfile.write(f"Li:{li_percent}")
    txtfile.write(f"O'Tooley:{otooley_percent}")
    txtfile.write(f"---------------------")
    txtfile.write(f"Winner: {winner}")
    txtfile.write(f"---------------------")
    txtfile.close()