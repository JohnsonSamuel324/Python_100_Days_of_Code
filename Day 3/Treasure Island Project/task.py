print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Game Logic
user_direction = input("Left or Right?\n")
if user_direction == "Right":
    print("You fell into a hole.")
    print ("GAME OVER.")
else:
    user_action = input("Would you like to swim or wait?\n")
    if user_action == "swim":
        print("You were attacked by a trout.")
        print("GAME OVER.")
    else:
        user_door = input("Which door would you like to enter, the red, yellow, or the blue door?\n")
        if user_door == "red":
            print("You are burned by fire.")
            print("GAME OVER.")
        elif user_door == "yellow":
            print("You found the treasure!")
            print("YOU WIN.")
        elif user_door == "blue":
            print("You were eaten by beasts.")
            print("GAME OVER.")
        else:
            print("You died trying to decide which door to open.")
            print("GAME OVER.")
