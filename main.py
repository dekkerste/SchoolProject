#!venv/bin/python3
import json

import cv2
import numpy as np
import requests as requests
from flask import Flask, render_template, request, flash, redirect, Response
from djitellopy import tello
# Imports the drone commands. This is used as a shortcut from control.py
try:
    from python.control import drone
except ImportError:
    print('Error while trying to import "control.py"')

app = Flask(__name__)
app.secret_key = '1234'

@app.route("/", methods=['GET', 'POST'])
def index():  # the message var needs to be set to zero
    return render_template("index.html")


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    print('connecting to drone')
    try:
        drone.connect()
        print('The drone is connected!')
    except:
        print('something went wrong')
    return render_template("index.html")


@app.route('/takeoff', methods=['GET', 'POST'])
def takeoff():
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


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
