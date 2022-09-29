from djitellopy import Tello

drone = Tello()
drone.connect()

drone.takeoff()
drone.get_battery()

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

move_right(180)
move_left(180)
drone.land()