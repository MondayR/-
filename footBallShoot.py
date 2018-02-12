# coding: utf-8
from random import choice

direction = [4,5,6]
yourGoal = 0
yourCatch = 0
ComputerGoal = 0
ComputerCatch = 0
print("now you Start the game!")
print("=============you kick===============")
for i in range(5):
	print("Choice a side to shoot you ball!")
	print("left:4,center:5,right:6")
	yourpick = input("your choice:")
	CmpPick = choice(direction)
	if (yourpick == CmpPick):
		print("Oops...")
		ComputerCatch += 1
	else:
		print("Goal!")
		yourGoal += 1
print("=============you Save===============")
for i in range(5):
	print("Choice a side to catch the ball!")
	print("left:4,center:5,right:6")
	yourpick = input("your choice:")
	CmpPick = choice(direction)
	if(yourpick == CmpPick):
		print("Saved!")
		yourCatch += 1
	else:
		print("Oops...")
		ComputerGoal += 1
if((yourGoal+yourCatch) == (ComputerGoal+ComputerCatch)):
	print("=========Equar Source,Adding Round===========")
	chk = raw_input("it's your last chance!take a shoot?(n/y):")
	print("choose a side")
	yourpick = input("your choice:")
	CmpPick = choice(direction)
	if(chk == 'y'):
		if(yourpick == CmpPick):
			print("Oops...")
			ComputerCatch += 1
		else:
			print("Goal!")
			yourGoal += 1
	else :
		if(yourpick == CmpPick):
			print("Saved!")
			yourCatch += 1
		else:
			print("Oops...")
			ComputerGoal += 1
if((yourGoal + yourCatch)>(ComputerGoal + ComputerCatch)):
	print("")
	print("YOU WIN!")
else:
	print("")
	print("YOU LOSE!")