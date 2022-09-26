from djitellopy import Tello

drone = Tello()
drone.connect()

drone.takeoff()
drone.get_battery()

def speed():
    drone.get_speed_x()
    drone.get_speed_y()

def emergency():
    drone.emergency()

def battery():
    drone.get_battery()

def move_up():
    drone.move_up()

def move_down():
    drone.move_down()

def move_left():
    drone.move_left()

def move_right():
    drone.move_left()
