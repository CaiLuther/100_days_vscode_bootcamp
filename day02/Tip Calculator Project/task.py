print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
per_person_final = round(((tip * 0.01) * bill + bill) / people, 2)

print(f"Each person should pay {per_person_final}")
