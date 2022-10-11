#!venv/bin/python3
import json

import cv2
import numpy as np
# import requests as requests
from flask import Flask, render_template, request, flash, redirect, Response, url_for
from djitellopy import tello
# Imports the drone commands. This is used as a shortcut from control.py


app = Flask(__name__)
app.secret_key = '1234'

#@BUG

@app.route("/", methods=['GET', 'POST'])
def index():  # the message var needs to be set to zero
    # request.script_root = url_for('index', _external=True)
    return render_template("index.html")


@app.route('/connect', methods=['GET', 'POST'])
def connect():
    try:
        drone.connect()
        return {"message": "the drone is connected."}
    except:
        # Returns a JSON object which is later used in AJAX to display a message on the webpage.
        return {"message": "[ERROR]: Something went wrong connecting to the drone."}


@app.route('/flysquare', methods=['GET', 'POST'])
def flysquare():
    try:
        drone.connect()
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


# set export FLASK_APP=main.py before running
if __name__ == "__main__":
    print('[INFO]' + ' ' + 'main.py is running')
    app.run(host="127.0.0.1", port=8000, debug=True)
