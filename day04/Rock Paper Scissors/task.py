import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gang_sign = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors: "))
print(user_choice)

computer_choice = random.randint(0,2)

result = ''

if user_choice == computer_choice:
   result = 'You Tied.'
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or(user_choice == 2 and computer_choice == 0):
    result = 'You Lost :('
elif (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1) or(user_choice == 0 and computer_choice == 2):
    result = 'You Won!'


if user_choice == 0:
    user_choice = gang_sign[0]
elif user_choice == 1:
    user_choice = gang_sign[1]
elif user_choice == 2:
    user_choice = gang_sign[2]

computer_choice = gang_sign[computer_choice]
print(f"{computer_choice} \nComputer chose ^" )

print(f"{user_choice}\nUser chose ^" )

print(f"\nResult: {result}")




 


# print(f"Computer Chose: {computer_choice}")

# print(f"You chose: {user_choice}")




        