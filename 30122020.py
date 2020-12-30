
choice = "-" 
#Stamaei to programma
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list")
        print("1: \tLearn Python")
        print("2: \tLearn Java")
        print("3: \tLearn CSS3")
        print("4: \tGo for a coffee")
        print("5: \tGo kill Snik")
        print("0: \tExit")

    choice = input()

