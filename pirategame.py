from pirateimageload import logoload
from pirateimageload import shopownerload

coins = 99999999999999999
crewmember = 1
shipstatus = "no ship"
maxcrew = 1

def startgame():
    logoload()
    print("""WELCOME TO SEADOGS AND SCALLYWAGS! A GAME ABOUT TREASURE AND THROWING MONEY AT YOUR PROBLEMS!
    
        HOW TO PLAY:
        ===========
        - You start out with 0 gold and 1 crew member (yourself), and no ship. 
        As soon as you max out both, you win the game.
        - Your objective is to get the best ship and a full crew. The best ship is a warship, which can hold a maximum of 4 crew members.
        - You will explore islands to get enough gold to buy these things from the shop. However, there is a chance you can lose a crew member due to risk. 
        A better ship will decrease this risk.
                        * To access the shop, type '1' in the console. 
        - When risk goes bad, you will lose a crew member. When you reach 0 crew members, you lose the game.
        """)

def mainmenu():
    global coins
    global crewmember
    global shipstatus
    global maxcrew
    choice = input("""What do you wish to do?
    [1] Go to Davey Jones' Locker Store
    """)
    if choice == "1":
        shop()

def shop():
    global coins
    global crewmember
    global shipstatus
    global maxcrew
    shopownerload()
    coins = int(coins)
    nextship = ""
    maxcrew = ""

    if shipstatus == "no ship":
        nextship = "raft"
        maxcrew = 1
    elif shipstatus == "raft":
        nextship = "sailing boat"
        maxcrew = 2
    elif shipstatus == "sailing boat":
        nextship = "warship"
        maxcrew = 3
    elif shipstatus == "warship":
        maxcrew = 4

    print("""YE ENTER THE DAVEY JONES' LOCKER SHOP? WISH TO BUY A SHIP UPGRADE? MORE BODIES 
    TO FUEL YER SELFISH TREASURE SEEKING SELF? GIMME THOSE DOUBLOONS AND YOU'LL GET WHAT YE WANT.
    """)
    shopoption = input(f"""You have {str(coins)} coins, {str(crewmember)} crew members left, and you have {shipstatus}.
                       [2] Go back to Main Menu
                       [3] Upgrade Ship [{nextship}] 
                       [4] Hire a Crewmember [10 COINS]""")
    if shopoption == "2":
        mainmenu()
    elif shopoption == "3":
        if coins < 20:
            print("YA DON'T GOT ENOUGH TO BUY THIS BEAUTY OF A SHIP. COME BACK WHEN YOU GOT MORE DOUBLOONS.")
        if nextship == "raft":
            print(f"""That'll BE TWENTY DOUBLOONS. YOU HAVE {coins} DOUBLOONS LEFT!
            - Your max crew members will increase to two.
            - Your chances of danger will decrease by ten percent, and your chances of finding treasure will be increased by ten percent.""")
            input(f"""
            [1] YAY
            [2] NAY""")
            shipstatus = "raft"
            coins = coins - 20
            maxcrew = 2
            shop()

        if nextship == "sailing boat":
            if coins < 50:
                print("YA DON'T GOT ENOUGH TO BUY THIS BEAUTY OF A SHIP. COME BACK WHEN YOU GOT MORE DOUBLOONS.")
            print(f"""That'll BE FIFTY DOUBLOONS. YOU HAVE {coins} DOUBLOONS LEFT!
            - Your max crew members will increase to three.
            - Your chances of danger will decrease by twenty percent, and your chances of finding treasure will be increased by twenty percent.""")
            input(f"""
            [1] YAY
            [2] NAY""")
            coins = coins - 50
            print("NICE DEALING BUSINESS WITH YE")
            maxcrew = 3
            shipstatus = "sailing boat"
            shop()

        if nextship == "warship":
            if coins < 100:
                print("YA DON'T GOT ENOUGH TO BUY THIS BEAUTY OF A SHIP. COME BACK WHEN YOU GOT MORE DOUBLOONS.")
            print(f"""That'll BE FIFTY DOUBLOONS. YOU HAVE {coins} DOUBLOONS LEFT!
            - Your max crew members will increase to three.
            - Your chances of danger will decrease by twenty percent, and your chances of finding treasure will be increased by fifty percent.""")
            input(f"""
            [1] YAY
            [2] NAY""")
            coins = coins - 100
            print("NICE DEALING BUSINESS WITH YE")
            maxcrew = 4
            shipstatus = "warship"
            input()
            shop()

        if shipstatus == "warship":
            print("I AINT GOT NO BIGGER SHIPS. GIT.")

    elif shopoption == "4":
        if coins < 10 and crewmember == maxcrew:
            print(
                f"BUT IT LOOKS LIKE YER DON'T GOT ENOUGH TO AFFORD ANY. A MERE {coins} DOUBLOONS YOU HAVE RIGHT NOW! COME BACK WHEN YA LOOT A CHEST OR SOMETHING.")
            input()
            shop()
        elif coins >= 10 and crewmember + 1 <= maxcrew:
            crewmember += 1
            coins -= 10
            print(f"""AYYYYY THAT'S WHAT I LIKE TO SEE. HERE IS ANOTHARR SCALLYWAG TO ADD TO YARRR CREW. YA GOT {crewmember} crew now!"
                              YA GOT {coins} DOUBLOONS LEFT!""")
            input()
            shop()
        elif coins >= 10 and crewmember + 1 > maxcrew:
            print(f"WOT? GO BUY A BIGGER SHIP FIRST. THAT {shipstatus} DINGY OF YOURS CAN ONLY FIT {maxcrew} CREW!")
            input()
            shop()
        elif crewmember + 1 > maxcrew and shipstatus == "warship":
            print("I DONT GOT NO BIGGER SHIPS LADDY. GIT.")
            input()
            shop()
    else:
        shop()
startgame()
mainmenu()