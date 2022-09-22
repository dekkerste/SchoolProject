from djitellopy import Tello

drone = Tello()
drone.connect()

drone.takeoff()
drone.get_battery()

def opdracht1():
    drone.get_battery()

def get_speed_x(self) -> int:
    return self.get_state_field('vgx')

    def get_speed_y(self) -> int:
    return self.get_state_field('vgy')