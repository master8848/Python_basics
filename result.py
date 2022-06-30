while True:
    AddOrSee = input("Do you want to see students(S) \n Do you want to add student(A)) \n To exit press(E)").upper()
    f = open("marks.txt","a+")
    if AddOrSee[0] == "A":
        name=input("What is Student's full name: ")
        #lname=input(f"what is {fname}'s last name: ")
        mark=name + "  "
        for x in range(0,3):
            subject =["Science","Maths","English"]

            marks=(input(f"Enter {name}'s mark in {subject[x]}: " ))
            mark+=marks +"  "
        mark+= "\n"
        f.write(mark)
    elif AddOrSee[0] == "S":
        for x in f:
            print(x)
    elif AddOrSee[0] == "E":
        f.close()
        exit()
    else :
        print("Please enter a valid value")

   