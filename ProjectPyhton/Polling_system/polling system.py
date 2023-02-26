# taking input as nominee what we want to keep
nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2nd nominee: ")

#taking vote count for both must be 0
nm1_votes = 0
nm2_votes = 0
voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)
while True:
    if voter_id == []: # to check when voter list is completed
        print("Voting session is over!!") 
        if nm1_votes > nm2_votes :
            percent = (nm1_votes/no_of_voter)*100 
            print(nominee1,"has won the elections with",percent,"%")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100 
            print(nominee2,"has won the elections with",percent,"%")
            break
        else :
            print("Both have equal number of votes! Therefore, it will be a coilation government.")
            break

    voter = int(input("Enter your voter id: "))
    if voter in voter_id:
        print("You are a voter!")
        voter_id.remove(voter)  # it will remove so that again same voter can't vote
        print("---------------------------------------") 
        print("To give vote to ", nominee1, ",Press 1 ")
        print("To give vote to ", nominee2, ",Press 2 ")
        print("----------------X-----------------------")
        vote = int(input("Enter your vote: "))
        if vote == 1:
            nm1_votes += 1
            print(nominee1,",Thankyou for your vote!")
        elif vote == 2:
            nm2_votes += 1
            print(nominee2,",Thankyou for your vote!")
        elif vote > 2:
            print("Check your pressed key!")
        else:
            print("You are not a voter OR You have already voted !")