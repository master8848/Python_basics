import random
l=[]
k=0
while (k<10000) :
	k=k+1
	for i in range(10):
		l.append(random.randint(10000000,99999999))

	#print(l)
	#if 100 in l:
	#	print("100 is in random intigers")
	#	c=l.count(100)
	#	print(f"count of 100 {c}") 
	#elif 1 in l:
	#	print("1 is in random integers")
	#	c=l.count(1)
	#	print(f"count of 1 {c}") 
	
	for i in range(10):
		for j in range(10):
			if i==j:
				pass
			elif l[i]==l[j]:
				print("you won a lottary")
				
print("Did you win")			

