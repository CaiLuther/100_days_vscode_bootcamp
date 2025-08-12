# S = 15, M = 20, L = 25
# S pep = +2, M/L +pep = +3
# all size xtra chz = +1
# print(f"Your bill is {bill}")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    else:
        print("You fucked up one of the add on options")
    print(f"Your small pizza will be ${bill}")
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    else:
        print("You fucked up one of the add on options")
    print(f"Your medium pizza will be ${bill}")
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your large pizza will be ${bill} fatty")
else:
    print("you fucked up the size")
