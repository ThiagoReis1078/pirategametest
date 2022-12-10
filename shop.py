def pirategame():
    global coins
    global crewmember
    global shipstatus
    choice = input("""What do you want to do?
        [1] Visit the Davey Jones Locker Shop
        [2] Go on an Adventure For Gold
        [3] End The Game\n""")
    if choice == 1:
        shop()
    if choice == 2:
        print("THIS PART OF THE GAME IS STILL UNDER DEVELOPMENT.")
    if choice == 3:
        print("Thank you for playing!")
    else:
        choice = input("""What do you want to do?
                [1] Visit the Davey Jones Locker Shop
                [2] Go on an Adventure For Gold
                [3] End The Game\n""")
