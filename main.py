#!/usr/bin/env python
# -*- coding: utf-8 -*-

# install python packages in the requirements.txt file:
# pip install requirements.txt

import logging
# import cv2
from djitellopy import tello
import time
# https://flask.palletsprojects.com/en/2.2.x/installation/
# Use a virtual environment to manage the dependencies for your project, both in development and in production.
#
# What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need
# to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one
# project can break compatibility in another project.
#
# Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one
# project will not affect other projects or the operating system’s packages.
from flask import Flask
from flask import Flask, render_template
import pyscreenshot
import random
import string


logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/dronetakeoff', methods=['POST'])
def dronetakeoff():
	# Connects to the Drone. A Wi-Fi connection to the Drone is required
	drone = tello.Tello()
	drone.connect()
	return render_template('show.html')


if __name__ == '__main__':
	# Only run the program if  the name of the file is main.py
	# sets the debugger from flak to enable autoreload
	app.run(debug=True)
	app.config['ENV'] = 'development'
	app.config['DEBUG'] = True
	app.config['TESTING'] = True
	# Uses a debugger to show error messages
	logging.basicConfig(level=logging.DEBUG)  # Based on pep, witch is also used in PyCharm
	logger.info("main.py logger")

	# Connects to the Drone
	# connect()
	# Shows a message that the app has started
	print('The application has started')
	# auto reload page on code change
