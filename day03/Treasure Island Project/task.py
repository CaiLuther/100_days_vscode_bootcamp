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
    f"\nYou reach an enchanted forest with two entrances.\nWhich direction will you choose? Answer 'Right' or 'Left': "
)

if forest_direction == "Right":
    print(
        f"\n You went {forest_direction} and narrowly avoided death by fairy."
        f"\n\n-------------------------------------------------------------------\n"
    )
    lake_choice = input(
        f"You run off hearing the fairies cackling in the distance..."
        f"\nYou then come across a lake that shimmers like diamonds."
        f"\nWill you wait and take a rest or swim accross? Answer 'Wait' or 'Swim': "
    )
    if lake_choice == "Swim":
        print(
            f"\n You decided to {lake_choice}, so you dive in but quickly notice vibrations so extreme you feel it in the water all around you..."
            f"\n You surface for air and get one last look at the sky before the lochness monster swallows you whole."
            f"\n You died."
            f"\n\n-------------------------------------------------------------------\n"
        )
    elif lake_choice == "Wait":
        print(
            f"\n You decide now is a good time to {lake_choice} and enjoy the stunning scenery while eating some snacks your mom packed you."
            f"\n Suddenly you feel what must be an earthquake."
            f"\n The lochness monster explodes out of the water threatening you with its gaping maw."
            f"\n You start to panic when a portal opens beneathe you and transports you into a room with three doors."
            f"\n\n-------------------------------------------------------------------\n"
        )
        door_choice = input(
            f"You run off hearing the fairies cackling in the distance..."
            f"\nYou then come across a lake that shimmers like diamonds."
            f"\nWill you wait and take a rest or swim accross? Answer 'Wait' or 'Swim': "
        )
    else:
        print(
            f"\n The lochness monster peeks up out of the water and berates you for your incompetance in entering correct input."
            f"\n You feel shame so deep you can't go on. You slowly starve as you waste away."
            f"\n You died."
            f"\n\n-------------------------------------------------------------------\n"
        )

elif forest_direction == "Left":
    print(
        f"\n You went {forest_direction}, and fairies ate your flesh."
        f"\n You died."
        f"\n\n-------------------------------------------------------------------\n"
    )

else:
    print(
        f"\n Fairies bound you and stripped your flesh from your bones as a punishment for your incompetance in entering correct input."
        f"\n You died."
        f"\n\n-------------------------------------------------------------------\n"
    )
