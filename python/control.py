from djitellopy import Tello

drone = Tello()
drone.connect()

drone.takeoff()
drone.get_battery()

def opdracht1():
    drone.get_battery()

