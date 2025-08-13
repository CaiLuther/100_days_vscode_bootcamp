import random
import my_module

# x = random.randint(1, 10)
# print(x)
# print(my_module.my_favorite_number)

# y = random.random()  # does not include 1
# print(y)

# z = random.uniform(1, 10)  # includes upper bound
# print(z)

# print("Heads")
# print("Tails")

coin_int = random.randint(0, 1)

if coin_int == 0:
    print("Heads")
else:
    print("Tails")
