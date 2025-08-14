# def my_function():
#     print("hi")

# for x in range(5):
#     my_function()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
for x in range(1,14):
    jump()
    