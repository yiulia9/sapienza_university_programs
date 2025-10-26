def op():
    start = input("Press START to play\n")

    if start == "START":
        return menu()
    else:
        quit=input("Do you want to quit the game?\nY/N?\n")

        if quit=="N":
            return op()
        elif quit=="Y":
            return
            
def menu():
    select= int(input("1. Story\n2. Character\n3. Quit"))

    if select == 1:
        return story()
    elif select == 2:
        return char()
    elif select==3:
        return op()

def story():
    print("Temporary story")
    done=input("Stop reading?\nY/N\n")

    if done=="Y":
        return menu()
    elif done=="N":
        secret=input("You found a piece of paper in between the pages...\nPress MENU to go back\n")

        if secret=="MENU":
            return menu()
        else:
            return
    
    return

chars={
    "name":None,
    "class":None, 
    "hp":100,
    "mana":100,
    "speed":100
}
classes=[
    ("nitwit",{
        "hp":100,
        "mana":100,
        "speed":100
    }),
    ("knight",{
        "hp": 150,
        "mana": 100,
        "speed": 75
    }),
    ("mage",{
        "hp":75,
        "mana":150,
        "speed":100
    }),
    ("archer",{
        "hp":100,
        "mana":75,
        "speed":150
    })
]

def char():
    menuc=int(input("Welcome to your character sheet!\n1. View your stats\n2. Customize your character"))

    if menuc==1:
        print(chars)
    elif menuc==2:
        print("Let's start with your name shall we?")
        name=input("How would you like to be called?\n")
        chars["name"]=name
        print("Nice to meet you", name, ", what a beautiful name!\nNow what is your class adventurer?")
        print("""
        "There are three specializations from which you could choose!
        ...or you could choose none I guess...
        
        1. Nitwit
        2. Knight
        3. Mage
        4. Archer"       
               """)
        cl = int(input("\nPress the corresponding number to select your class:\n")) - 1
        chars["class"]=classes[cl][0]
        chars["hp"]=classes[cl][1].get("hp")
        chars["mana"]=classes[cl][2].get("mana")
        chars["speed"]=classes[cl][3].get("speed")






