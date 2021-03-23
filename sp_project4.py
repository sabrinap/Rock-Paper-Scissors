# ==============================================================================
# PROGRAM Rock, Paper, Scissors
# PROJECT NUMBER: 4 
# DUE DATE: Tuesday 11/05/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# Write a program which simulates the game of rock, paper, scissors.
# In this game, two people simultaneously choose either rock, paper, or scissors.
# Wether or not a play wins depends not only on what he or she chooses but also
# on what his or her opponent chooses.
#
# Paper covers rock, paper wins
# Scissors cut paper, scissors wins
# Rock breaks scissors, rock wins
# All matching combinations are ties
#
# Your program must simulate the play of this game, with the following
# considerations: each player starts with $100. When a player loses, he/she must
# pay the other player $10. A tie results in no exchange of money.
# Write your program so that the game is played repeatedly until ither (1) one
# player has no money left or (2) the game has been played 20 times. 
#
# INPUT
#
# This program asks the user for the choice of 1, 2 or 3, indicating
# Rock, Paper, or Scissors.  You must do error checking on this input
# and keep prompting the user until they enter a valid choice.
# You may assume that the user enters a number when asked for a number. 
#
# INPUT ERROR CHECKING
#
# Program must check for invalid command and negative numbers, and ask user to
# re-enter a value when necessary, until a valid data item is entered.
#
# OUTPUT
#
# The program prints an output menu, After each play of the game, print out
# the following in clear format: the choices each player made (print both the
# number giving the choice, and the word which describes it), which player won
# the game (or indicate a tie), and the amount of money each player has left.
# At the end of the program run print out a summary giving the total number of
# games actually played, the total number of games each player won, the number
# of tied games, the percentage of games won by each player, and the identity
# of the overall winner.
#
# ASSUMPTIONS
#
# We assume that input data is valid and correctly entered by the user.
# The program is guaranteed to warn user from invalid data entered and
# end program.
# ==============================================================================
# Import random module
import random

def main():
   #assign win, lose, and tie to zero for tallying
   win = 0
   lose = 0
   tie = 0
   winner = ''
   
   # Constant Variable
   PLAYERS_MONEY = 100 # Player money
   COMPUTERS_MONEY = 100 # Computer money
   
   printIntro() #prints welcome message and rules
   
   #While loop to make sure the game ends when one of the players reaches $0 or
   #they have played 20 rounds
   while(PLAYERS_MONEY > 0 and COMPUTERS_MONEY > 0 and (win+lose+tie) < 20):
       player_choice = playerChoose()
       computer_choice = computerChoose()
       
       #determines who won
       result = moveResult(player_choice, computer_choice)

      #Does math to deduct and add money depending on who won the round 
       if result == 'win':
           win += 1
           PLAYERS_MONEY += 10
           COMPUTERS_MONEY -= 10
           winner = 'Player 1!'
       elif result == 'lose':
           lose += 1
           PLAYERS_MONEY -= 10
           COMPUTERS_MONEY += 10
           winner = 'Player 2!'
       else:
           tie += 1
           winner ='Tie !'
       results(player_choice, computer_choice, winner, PLAYERS_MONEY, COMPUTERS_MONEY)  
          
   finalResults(result, win, lose, tie)      
  
# #############################################################################
def printIntro():
    
   # This function simply prints our a welcoming message and some initial
   # information to the user about how the program works.
   print ("\t----------=====******=====----------")
   print ("\t\tRock, Paper, and Scissors")
   print ("\t----------=====******=====----------")
   print (" This program plays the EXCITING game of Rock, Paper,")
   print ("and Scissors. Two players choose either Rock, Paper or Scissors,")
   print ("and the results of their picks are compared. Each match is")
   print ("determined as follows:")
   print ("\n\tPlayer 1 Player 2 Result")
   print ("\t-------- -------- ------")
   print ("\tRock Paper Paper covers Rock. Player 2 wins!")
   print ("\tPaper Scissors Scissors cut Paper. Player 2 wins!")
   print ("\tScissors Rock Rock breaks Scissors. Player 2 wins!")
   print ("\t--- --- Any matching combo. A tie!")
   print ("\n Now you are about to play a against world-class computer")
   print ("champion Dr. Windows. You are Player 1, and the computer")
   print ("is Player 2. Player 2's moves are randomly chosen by the computer.")
   print ("Both players start with $100 and the game is finished when either one")
   print ("player")
   print ("reaches $0 or there have been 3 matches played. The bet per match is $10.\n")
   #playerChoose()
  
# #############################################################################
def playerChoose():
    
   #getting user input
   userInput = int(input("\tPlayer 1, Enter choice of\n\t\t1. Rock\n\t\t2. Paper\n\t\t3. Scissors -> "))
   while userInput > 3 or userInput < 1:
       userInput = int(input("\tEnter valid input: "))
   if userInput == 1:
      # 1 is equvalent to rock
       userInput_name = 'ROCK'
   elif userInput == 2:
       # 2 is equvalent to paper
       userInput_name = 'PAPER'
   else:
       # 3 is equvalent to scissors
       userInput_name = 'SCISSORS'
       
   return userInput_name #return value

# #############################################################################
def computerChoose():
    
   # Computer picks randomly any number
   # between 1 , 2 and 3.
   comp_choice = random.randint(1, 3)
   
   # initialize value of comp_choice_name
   # variable corresponding to the choice value
   if comp_choice == 1:
       # 1 is equvalent to rock
       comp_choice_name = 'ROCK'
   elif comp_choice == 2:
       # 2 is equvalent to paper
       comp_choice_name = 'PAPER'
   else:
       # 3 is equvalent to scissors
       comp_choice_name = 'SCISSORS'
       
   return comp_choice_name

# #############################################################################
def moveResult(player_choice, computer_choice):
    
   #using if elif to identify who wins depending on what choice each player made
   if computer_choice == player_choice:
       result = 'tie'
   elif computer_choice == 'SCISSORS' and player_choice == 'ROCK':
       result = 'win'
   elif computer_choice == 'PAPER' and player_choice == 'SCISSORS':
       result = 'win'
   elif computer_choice == 'ROCK' and player_choice == 'PAPER':
       result = 'win'
   else:
       result = 'lose'
   #returns results of the move   
   return result  
      
# #############################################################################  
def results(player_choice, computer_choice, winner, PLAYERS_MONEY, COMPUTERS_MONEY):  

   print ("\nRESULTS OF THIS MOVE")
   print ("=-=-=-=-=-=-=-=-=-=-")
   print ("Player 1        Player 2              Player 1's  Player 2's")
   print ("Number  Action  Number  Action  Winner  Money  Money")
   print ("------  ------  ------  ------  ------  -----  -----")

  #print out the results of the move depending on what number each player has
   resultStr = ''
   if player_choice == 'ROCK':
       resultStr = '1\t'
   elif player_choice == 'PAPER':
       resultStr = '2\t'
   else:
       resultStr = '3\t'
   resultStr += player_choice+'\t'  
   if computer_choice == 'ROCK':
       resultStr += '1\t'
   elif computer_choice == 'PAPER':
       resultStr += '2\t'
   else:
       resultStr += '3\t'
   resultStr += computer_choice+'\t'
   
   #prints how much money each player has left won or lost each round
   resultStr += winner+'\t'+str(PLAYERS_MONEY)+'\t'+str(COMPUTERS_MONEY)
  
   print(resultStr)
   print("")
      
   #playerChoose()
  
###############################################################################
def finalResults(result, wins, lose, tie):

   #Prints out the stats of the game
   print ("\n\n----------=====******=====----------")
   print("\nAnd there you have it, folks, the final matchoff between our two")
   print("contestants. The final results for tonight's game are as follows:")
   print("\n\t\t\tPlayer 1 Player 2")
   print("\t\t\t======== ========")
   print("\tGames Won:\t %d\t%d" %(wins,lose))
   print("\tPercent Won:\t %.1f\t%.1f" %((float(wins*100))/(wins+lose+tie),(float(lose*100))/(wins+lose+tie)))
   print("\n\tTotal games tied: %d" %(tie))
   print("\n\tTotal games played: %d" %(wins+lose+tie))
   
   #prints out overall winner
   if wins > lose:
       print("\n\tThe overall winner is Player 1!")
   elif wins < lose:
       print("\n\tThe overall winner is Player 2!")
   else:
       print("\n\tThe overall winner is Tie!")
   print("\nStop in again soon to play another exciting match!!!")
   print("\n----------=====******=====----------")
   
main()  
