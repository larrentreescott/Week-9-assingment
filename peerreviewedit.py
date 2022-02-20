# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Scott Larrentree
# Creation Date: 02/11/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#	print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')

	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')

# take out the tab making out look cleaner

	print()

def chooseCave():
    cave = ''
    
#    while cave != '1' and cave != '2':
    while cave != '1' and cave != '2':
#the tab used proir was causing an error so i changed it to 4 spaces

        #print('Which cave will you go into? (1 or 2)')
        #cave = input()
        print('Which cave will you go into? (1 or 2)')
        cave = input()
        # had to fix indentation on both of these lines was throwing errors
        

	#return caves
    return cave
	# caves is incorrect variable changed cave also had to fix indentation previous tab made caused and error

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	
	#time.sleep(3)
	time.sleep(2)
	#wants to sleep for 2 seconds so changed 3 to 2
	
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
	    
		#print 'Gobbles you down in one bite!'
		print ('Gobbles you down in one bite!')
		# print needs to have ()

playAgain = 'yes'


#displayIntro()
displayIntro()
#take displayIntro out of the while loop


#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
# This line was setting the variable not comparing.


	
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	# function name is choosenCave not choosencave
	
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	
	
	if playAgain == "no":
		print("Thanks for planing")

