#Candidates Selected for elections
nominee_1=input("Enter the nominee 1 name:")
nominee_2=input("Enter the nominee 2 name:")
#initial votes counted for each nominee
nom_1_votes=0
nom_2_votes=0
#now we create a voter id list
votes_id=[1,2,3,4,5,6,7,8,9,10]  #10 people are going to vote in this election
#gives the length of number of voters
number_of_voter=len(votes_id)
while True:
    if votes_id==[]:
        print("Voting Session Completed")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/nom_2_votes)*100
            print(nominee_1,"hase won with",percent,"% votes")
            break

        elif nom_2_votes>nom_1_votes:   #count the number of votes and give its percentage
            percent=(nom_2_votes/nom_1_votes)*100
            print(nominee_2,"has won with",percent,"% votes")
            break

    else:
        voter=int(input("Enter Your Voter Id No:"))
        if voter in votes_id:
           print("You are a Voter")
           votes_id.remove(voter)  #after voting the voter cannot vote again!!!
           vote=int(input("Enter your vote 1 or 2:"))
           if vote==1:
               nom_1_votes+=1
               print("Thank You")

           elif vote==2:
            nom_2_votes+=2
            print("Thank You")
        else:
            print("your are not a voter here / You have already voted")
             #if the voter Id is not present the we print this message
