street_tool = 15
street = ["-"for i in range(street_tool)]
car_x = 0
Car = "X"

street[car_x] = Car 

def print_street():
    row = "|" + "|".join(map(lambda x: x.center(3), street)) + "|"
    print(row)

print_street()

def can_move(new_x):
    valid_move = True
    if 0 <= new_x < street_tool:
        return valid_move
    else:
        print("can not move")
        valid_move = False
        return valid_move

def move(new_x):
    global car_x
    street[car_x] = "-"
    car_x = new_x
    street[car_x] = Car

def move_right():
    new_x = car_x + 1
    if can_move(new_x):
        move(new_x)

def move_left():
    new_x = car_x - 1
    if can_move(new_x):
        move(new_x)

controller = {
    "R":move_right,
    "L":move_left
}
while True:
    print_street()
    jahat = input("kodoom var? (R/L)").upper()
    result = controller.get(jahat)
    result()
