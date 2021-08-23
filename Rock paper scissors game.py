#pylint:disable=E1111
#import library
import random
#function for random number
def rand():
	number= [1,2,3]
	n=random.choice (number)
	return int (n)
#option choose function
def option (n):
	if (n==1):
		print("\t'ROCK'")
	if (n==2):
		print ("\t'PAPER'")
	if (n==3):
		print ("\t'SCISSOR'")
#big function:
def big (a,b):
	if (a==1 and b== 2):
		print ("     Computer Win")
		return 0
	elif (a==2 and b==1):
		print ("      You Win")
		return 1
	elif (a==1 and b==3):
		print ("      You Win")
		return  1
	elif (a==3 and b== 1):
		print ("      Computer Win")
		return 0
	elif (a==2 and b==3):
		print ("      Computer Win")
		return 0
	elif (a==3 and b== 2):
		print ("      You Win")
		return  1
	else:
		print ("      It's a Draw")
		return -1
	
# main function:
print("****** Welcome to the Game *******")
print ("  ~ ROCK PAPER SCISSOR ~")
print ("          ©RKB GAMES")
print ("\n")
your_score=0
computer_score=0

for i in range (3):
	print ("\n")
	print ("\t>> Your turn :")
	your_option=int(input("choose\n 1 for 'ROCK'\n 2 for 'PAPER'\n 3 for 'SCISSOR'\n"))
	if (your_option>3):
		print ("🔴 INVALID")
		break
	
	print ("you choose:")
	your_choise=option(your_option)
	print ("\t>>Computer's Turn:")
	print ("Computer choose:")
	computer_option = rand()
	computer_choise=option(computer_option)
	print("~~~~~~~~~~~~~~~~~~~")
	x= big (your_option,computer_option)
	print("~~~~~~~~~~~~~~~~~~~")
	your_score=int (your_score)
	computer_score=int (computer_score)
	if (x==1):
		your_score=your_score+1
	elif (x==0):
		computer_score=computer_score+1
	else:
			your_score=your_score+1
			computer_score=computer_score+1

				
print ("\t \t >>> Score Bord<<<")
print("        YOU:",your_score)
print ("       COMPUTER:", computer_score)
print("\n")
print("~~~~~~~~~~~~~~~~~~~")
if (your_score>computer_score):
			print("Congratulations 🎉 YOU WIN")
elif (computer_score>your_score):
	print ("🙁 YOU LOOSE")
elif (your_score==computer_score):
	print("•Draw")
print("~~~~~~~~~~~~~~~~~~~")
			
	
	