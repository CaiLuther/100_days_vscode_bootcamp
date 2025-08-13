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
print(f"\n\n-------------------------------------------------------------------\n")
print(f"\nWelcome to Treasure Island.")
print("Your mission is to find the treasure, incorrect input will result in death.")
print(f"\n\n-------------------------------------------------------------------\n")


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
            f"\n Your peaceful reverie is broken when you feel what must be an earthquake."
            f"\n The lochness monster explodes out of the water threatening you with its gaping maw."
            f"\n You start to panic when a portal opens beneathe you and transports you into a room with three doors."
            f"\n\n-------------------------------------------------------------------\n"
        )

        door_choice = input(
            f"You take in your new surroundings and examine the three doors."
            f"\nTo the left is pale blue door, to the right is a dull yellow door, and straight in front of you is a bright red door"
            f"\nWhich door will you choose? Answer 'Blue', 'Yellow', or 'Red': "
        )

        if door_choice == "Red":
            print(
                f"\n You choose the inviting bright {door_choice} door, and timidly open it. A deep musty odor envelops you."
                f"\n Through the dim light you see the treasure! You move towards it and start to pry it open..."
                f"\n You notice something sharp on your fingers, but it is too late."
                f"\n A purple tongue lolls out between razor sharp teeth and wraps around you. The mimic devours you."
                f"\n You died."
                f"\n\n-------------------------------------------------------------------\n"
            )

        elif door_choice == "Yellow":
            print(
                f"\n You choose the dull {door_choice} door, and timidly open it. The air feels warm and inviting."
                f"\n Before you know it the door slams shut behind you."
                f"\n A trap opens and the room starts filling with sand and violent wind. The temperature climbs into an unbearable heat."
                f"\n The sand slowly crushes and suffocates you until the room becomes your tomb."
                f"\n You died."
                f"\n\n-------------------------------------------------------------------\n"
            )

        elif door_choice == "Blue":
            print(
                f"\n You open the pale {door_choice} door."
                f"\n The room has an open ceiling where the sunlight rains down onto a glimmering gold treasure box!"
                f"\n You pry it open to find unimaginable wealth."
                f"\n Another portal opens up and you walk through it to find you're now at home with the treasure."
                f"\n You pay off your mom's mortgage and spend the rest on blackjack and hookers."
                f"\n Congratulations, you lived!"
                f"\n\n-------------------------------------------------------------------\n"
            )

        else:
            print(
                f"\n The walls start to move quickly closing in on you."
                f"\n There is an exit you could run out of, but you can't even enter the correct input, so you're clearly too stupid to run for the exit."
                f"\n The walls crush you while you stand there drooling."
                f"\n You died."
                f"\n\n-------------------------------------------------------------------\n"
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
