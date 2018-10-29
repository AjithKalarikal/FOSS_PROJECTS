#For importing random functioNs

import random
a=random.randint(1,3)
print("Welcome to Rock,Paper,Scissor game")
i=1
while i>0:
#inputing user decision
	print("Enter your Turn")
	print("press 1 for stone,press 2 for paper,press 3 for scissors")
	b=int(input())
#Printing Decisions
	i=0
	if b==1:
		print("Your Decision=ROCK")
	elif b==2:
		print("Your Decision=PAPER")
	else:
		print("Your Decision=SCISSORS")
	
	if a==1:
		print("Comp Decision=ROCK")
	elif a==2:
		print("Comp Decision=PAPER")
	else:
		print("Comp Decision=SCISSORS")

#Game Process

	if (a==1)and(b==3):
		print("Computer won")
	elif (a==1)and(b==2):
		print("You won")
	elif (a==2)and(b==1):
		print("Computer won")
	elif (a==2)and(b==3):
		print("You won")
	elif (a==3)and(b==1):
		print("You won")
	elif (a==3)and(b==2):
		print("Computer won")
	else:
		print("Tie")
	print(" ")
	print(" ")

	print("press 1 to start again/ 0 to quit the game")
	i=int(input())
	

