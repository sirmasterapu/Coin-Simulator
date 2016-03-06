#Author: Apurva Memani
#Date: February 2, 2016
import random
prediction = raw_input("What do you think the coin will be? Please use heads or tails. ")
flip = random.randint(0,1)
#this makes the randomization of the coin flip
term = ("heads") 

term2 = ("tails")

#sets what terms we are looking for in prediction
if (flip == 0):
	print("The coin is Heads")
	
elif (flip == 1):
		print("The coin is Tails")
#tells what each side is
if term == prediction and (flip == 0):
	print("You are correct!")
	
elif term2 == prediction and (flip == 0):
	print("You are incorrect")
#checks if your prediction is right or wrong
if term == prediction and (flip == 1):
	print("You are incorrect!")

elif term2 == prediction and (flip == 1):
	print("You are correct!")
#checks if your prediction is right or wrong 