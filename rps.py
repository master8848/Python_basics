import random

condition=True

while condition:
	

	
	choice=["R","P","S"]
	computer_action=random.choice(choice)
	user_input=input("Rock(R)/Paper(P)/Sissior(s)").upper()
	user_action=user_input[0]
	if user_action == computer_action:
  	  print(f"Both players selected {user_action}. It's a tie!")
	elif user_action == "R":
 	   if computer_action == "S":
 	       print("Rock smashes scissors! You win!")
 	   else:
 	       print("Paper covers rock! You lose.")
	elif user_action == "P":
 	   if computer_action == "R":
 	       print("Paper covers rock! You win!")
 	   else:
 	       print("Scissors cuts paper! You lose.")
	elif user_action == "S":
	    if computer_action == "P":
 	       print("Scissors cuts paper! You win!")
	    else:
	        print("Rock smashes scissors! You lose.")

