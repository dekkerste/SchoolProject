from djitellopy import Tello

try:
    drone = Tello()
except:
    print('something went wrong setting drone var')

# drone.get_battery()



def speed():
    print(drone.get_speed_x())
    print(drone.get_speed_y())


def emergency():
    drone.emergency()


def battery():
    print(drone.get_battery())


def move_up():
    drone.move_up()


def move_down():
    drone.move_down()


def move_left(y: int):
    drone.move_left(y)


def move_right(x: int):
    drone.move_right(x)


def flip_left():
    drone.flip_left()


def flip_right():
    drone.flip_right()

def move_forward(a: int):
    drone.move_forward(a)


def move_back(b: int):
    drone.move_back(b)


move_forward(100)
move_right(100)
move_back(100)
move_left(100)
drone.land()
