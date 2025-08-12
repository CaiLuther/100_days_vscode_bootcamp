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
    print(f"You went {forest_direction} and narrowly avoided death by fairy. You died.")
    lake_choice = input(
        "You run off hearing fairies laugh knowingly in the background..."
        "you come across a lake that shimmers majestically. Will you wait and take a rest or swim accross? Answer  \
    'Wait' or 'Swim': "
    )
    if lake_choice == "Swim":
        print(
            f"You decided to {lake_choice} so you dive in, but quickly notice a shake so extreme you feel it through the water..."
            "you get one last look at the sky before the lochness monster swallows you whole. You died."
        )
if forest_direction == "Left":
    print(f"You {forest_direction} and, fairies ate your flesh.")
else:
    print(
        "Fairies ate you as a punishment for your incompetance in giving correct input. Learn to read."
    )
