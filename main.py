#!venv/bin/python3
import json

# import cv2
# import numpy as np
# import requests as requests
from flask import Flask, render_template, request, flash, redirect, Response, url_for
from djitellopy import Tello
# Imports the drone commands. This is used as a shortcut from control.py
from utils import *
import logging
Tello.LOGGER.setLevel(logging.DEBUG)

app = Flask(__name__)
app.secret_key = '1234'


@app.route("/", methods=['GET', 'POST'])
def index():  # the message var needs to be set to zero
    # request.script_root = url_for('index', _external=True)
    return render_template("index.html")


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    try:
        global drone
        print('try to connect')
        drone = initializeTello()
        return {"message": "the drone is connected."}
    except:
        # Returns a JSON object which is later used in AJAX to display a message on the webpage.
        return {"message": "[ERROR]: Something went wrong connecting to the drone."}


@app.route('/flysquare', methods=['GET', 'POST'])
def flysquare():
    try:
        drone.connect()
        move_forward(100)
        move_right(100)
        move_back(100)
        move_left(100)
        drone.land()
        return {"message": "The drone flys a square"}
    except:
        # Returns a JSON object which is later used in AJAX to display a message on the webpage.
        return {"message": "[ERROR]: Something went wrong"}

@app.route('/takeoff', methods=['GET', 'POST'])
def takeoff(drone=None):
    print('taking off the drone')
    try:
        drone.takeoff()
        print('The drone has taken off')
    except:
        print('something went wrong')
    return render_template("index.html")


@app.route('/customcommand', methods=['GET', 'POST'])
def customcommand():
    cust = request.form['customcommandcontents']
    print(cust)
    return render_template("index.html")


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


# set export FLASK_APP=main.py before running
if __name__ == "__main__":
    print('[INFO]' + ' ' + 'main.py is running')
    app.run(host="127.0.0.1", port=8000, debug=True)

