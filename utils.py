from djitellopy import Tello


def initializeTello():
    print('utlis imported.')
    drone = Tello()
    drone.connect()
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0
    print(drone.get_battery())
    drone.takeoff()
    drone.land()
    return drone

