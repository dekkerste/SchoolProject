from flask import Flask, render_template, request
from djitellopy import tello

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index(message=None):  # the message var needs to be set to zero
    if request.method == 'POST':
        if request.form.get('Connect') == 'Connect':
            print("Connecting to the drone...")
            message = 'Connecting to the drone...'  # This message will be shown in the webpage
            # try to run the drone connection. If it fails, shows it on the webpage.
            try:
                # connect()  # Starts a def where the drone connection code is
                print('i want to connect to the drone')
            except:
                print("Connection error")
                message = "Connection Error"
            pass
        elif request.form.get('TakeOff') == 'TakeOff':
            # pass # do something else
            print("Taking off the drone")
            message = "Taking of the drone..."
            pass
        else:
            return render_template("index.html")  # returns the same index.html if the buttons are not clicked
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html", message=message)



# Code block that holds the drone connection code.
def connect(message=None):
    drone = tello.Tello()
    drone.connect()
    print('The drone is connected!')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
