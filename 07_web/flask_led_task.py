from flask import Flask
import RPi.GPIO as GPIO
RED_PIN = 4
BLUE_PIN = 3
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''
@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == "red":
        if op=="on":
            GPIO.output(RED_PIN, GPIO.HIGH)
            return """
            <p> RED LED ON</p>
            <a href="/">Go Home</a>
            """
        elif op=="off":
            GPIO.output(RED_PIN, GPIO.LOW)
            return """
            <p> LED OFF</p>
            <a href="/">Go Home</a>
            """
    elif color =="blue":
        if op=="on":
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            return """
            <p> BLUE LED ON</p>
            <a href="/">Go Home</a>
            """
        elif op =="off":
            GPIO.output(BLUE_PIN, GPIO.LOW)
            return """
            <p> LED OFF</p>
            <a href="/">Go Home</a>
            """
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()