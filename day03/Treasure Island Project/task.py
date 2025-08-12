print(
    r'''
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
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure, incorrect input will result in death.")

forest_direction = input(
    "You reach an enchanted forest with two entrances. Which direction will you take? Answer 'Right' or 'Left': "
)
print(forest_direction)

if forest_direction == "Right":
    print(f"You went {forest_direction} and narrowly avoided death by fairy.")
    lake_choice = input(
        "\nYou run off hearing the fairies cackling in the background...\n"
        "You come across a lake that shimmers like diamonds.\n Will you wait and take a rest or swim accross? Answer 'Wait' or 'Swim': \n"
    )
    print(lake_choice)

    if lake_choice == "Swim":
        print(
            f"\nYou decided to {lake_choice} so you dive in, but quickly notice vibrations so extreme you feel it in the water all around you...\n"
            "You surgace for air and get one last look at the sky before the lochness monster swallows you whole. \n You died.\n"
        )
    elif lake_choice == "Wait":
        print(
            f"\nYou decide now is a good time to f{lake_choice} and enjoy the stunning scenery while eating some snacks your mom packed you.\ntyu7p;/p"
            "Suddenly you feel what must be an earthquake."
            "The lochness monster explodes out of the water threatening you with its gaping maw."
            "You start to panic when a portal opens beneathe you and transports you into a room with three doors"
        )
    else:
        print(
            "The lochness monster peeks up out of the water and berates you for your incompetance in entering correct input. You feel shame so deep you can't go on. You died."
        )

elif forest_direction == "Left":
    print(f"You went {forest_direction} and, fairies ate your flesh.")
else:
    print(
        "Fairies ate you as a punishment for your incompetance in entering correct input. You died."
    )
