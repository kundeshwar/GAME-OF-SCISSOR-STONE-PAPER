from multiprocessing import parent_process
import random 
l = ["Paper", "Scissor", "Rock"]
while True:
    comp = random.choice(l)
    user = int(input('''You are intersted to play. 
                                                       1.YES
                                                       2.NO
                                                            :-'''))
    if user == 1:
        user1 = int(input('''You chooice your Game standard :- 
                                                                1. THREE TURN
                                                                2. FIVE TURN
                                                            
                                                                          :-'''))
        if user1 == 1:
            userwin = 0
            userlose = 0
            tiecount = 0
            count = 0
            while True:
                user2 = int(input('''Enter your chooice:- 
                                                          1.Scissor
                                                          2.Paper
                                                          3.Rock
                                                                :-'''))
                if user2 == 1:
                    user3="Scissor"
                elif user2 == 2:
                    user3="Paper"
                else:
                    user3="Rock"    
                count += 1
                if comp == user3:
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print("YOU ARE NOT EITHER LOSE OR WIN, MATCH IS TIE!!!!")
                    print(count)
                    tiecount += 1
                elif ((user2 == 1)and(comp=="Paper")) or ((user2 == 2)and(comp=="Rock")) or ((user2 == 3)and(comp=="Scissor")):
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print(" IN THIS TURN YOU ARE WIN, CONGRAGULATION!!!!")
                    userwin += 1
                elif ((user2 == 2)and(comp=="Scissor")) or ((user2 == 3)and(comp=="Paper")) or ((user2 == 1)and(comp=="Rock")):
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print("IN THIS TURN YOU ARE LOSE,SORRY !!!!")
                    userlose += 1
                if count == 3:
                    if userwin == userlose :
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE is GOOD, BUT MATCH IS TIE. TRY ANOTHER TIME MAY HOPE CAN WIN!!!")
                    elif userwin < userlose:
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE is GOOD, BUT MATCH IS LOSE BY YOU. TRY ANOTHER TIME HOPE YOU CAN WIN!!!")
                    else:
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE IS GOOD, BUT MATCH IS WIN BY YOU. TRY ANOTHER TIME HOPE YOU CAN WIN!!!")
                    break

        elif user1 == 2:
            userwin = 0
            userlose = 0
            count = 0
            while True:
                user2 = int(input('''Enter your chooice:- 
                                                          1.Scissor
                                                          2.Paper
                                                          3.Rock
                                                                :-'''))
                if user2 == 1:
                    user3="Scissor"
                elif user2 == 2:
                    user3="Paper"
                else:
                    user3="Rock"    
                count += 1
                if comp == user3:
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print("YOU ARE NOT EITHER LOSE OR WIN, MATCH IS TIE!!!!")
                    print(count)
                elif ((user2 == 1)and(comp=="Paper")) or ((user2 == 2)and(comp=="Rock")) or ((user2 == 3)and(comp=="Scissor")):
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print(" IN THIS TURN YOU ARE WIN, CONGRAGULATION!!!!")
                    userwin += 1
                elif ((user2 == 2)and(comp=="Scissor")) or ((user2 == 3)and(comp=="Paper")) or ((user2 == 1)and(comp=="Rock")) :
                    print("COMPUTER CHOOICE:-",comp)
                    print("YOUR CHOOICE :-", user3)
                    print("IN THIS TURN YOU ARE LOSE,SORRY !!!!")
                    userlose += 1
                if count == 5:
                    if userwin == userlose :
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE is GOOD, BUT MATCH IS TIE. TRY ANOTHER TIME MAY HOPE CAN WIN!!!")
                    elif userwin < userlose:
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE is GOOD, BUT MATCH IS LOSE BY YOU. TRY ANOTHER TIME HOPE YOU CAN WIN!!!")
                    else:
                        print('''  
                                          ''')
                        print("YOUR LOST YOUR ALL TURNS, VIEW YOUR RESULT BELOW -----")
                        print("YOUR WIN COUNT:-", userwin)
                        print("YOU LOSE COUNT:-", userlose)
                        print("YOUR TIE COUNT :-", tiecount)
                        print("OVERALL YOUR PERFROMANCE IS GOOD, BUT MATCH IS WIN BY YOU. TRY ANOTHER TIME HOPE YOU CAN WIN!!!")
                    break
            
    elif user == 2:
        print("YOU CHOOICE TO EXIST FROM THE GAME, THANKS FOR PLAYING THIS GAME!!!!!!")
        break

                    

        

                
        