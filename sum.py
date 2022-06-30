#sum1=0
#for i in range(3):
#	
#	user=eval(input("Enter your numbers: "))
#	sum1+=user	
#print(f"Your sum was {sum1}")
sum1=0
while True:
	number=input("Enter the price or press q to quit: ")
	if not number[0] in ['o','y','n','q',"Q"]:
		sum1+=int(number)
		print(f"Your sum so far is {sum1}")
	else:
		print(f"Your sum was {sum1}")
		print("Thanks for using our Calculator")
		break
			
