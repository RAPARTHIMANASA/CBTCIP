import random 
l=["Rock","Paper","Scissor"]
'''
Rock vs Paper -> paper Wins
Rock vs Scissor -> Rock Wins
Paper vs Scissor -> Scissor
'''
while True:
    Computercount=0
    Usercount=0
    Userchoice=int(input('''Game Start...
     1.YES
     2.NO | EXIT '''))
    if Userchoice==1:
       for a in range(1,6):
         UserInput=int(input('''
1.Rock
2.Paper
3.Scissor'''))
         if UserInput==1:
            Userchoice="Rock"
         elif UserInput==2:
            Userchoice="Paper"
         elif UserInput==3:
            UserInput=="Scissor"
            Computerchoice=random.choice(l)
            if Computerchoice==Userchoice:
               print("computer value",Computerchoice)
               print("user value",Userchoice)
               print("Game Draw")
               Usercount=Usercount+1
               Computercount=Computercount+1
            elif (Userchoice=="Rock" and Computerchoice=="Scissor") or (Userchoice=="Paper" and Computerchoice=="Rock") or (Userchoice=="Scissor" and Computerchoice=="Paper"):
               print("Computer value",Computerchoice)
               print("user value",Userchoice)
               print("YOU WIN...!")
               Usercount=Usercount+1
            else:
               print("computer value",Computerchoice)
               print("user value",Userchoice)
               print("COMPUTER WIN...!")
               Computercount=Computercount+1
               if Usercount==Computercount:
                  print("Final Game Draw...")
                  print("user score",Usercount)
                  print("computer score",Computercount)
               elif Usercount>Computercount:
                  print("FINAL YOU WIN THE GAME...!")
                  print("user score",Usercount)
                  print("computer score",Computercount)
               else:
                  print("COMPUTER WIN THE GAME...!")
                  print("user score",Usercount)
                  print("computer score",Computercount)
         else:
            break


