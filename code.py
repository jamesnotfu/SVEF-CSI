import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

pwm = pwmio.PWMOut(board.A2, frequency=50)
my_servo = servo.ContinuousServo(pwm)

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        my_servo.throttle = 1.0
        print("forward")
    if cp.button_b:
        while(cp.button_b):
            pass
        my_servo.throttle = 0.0
        print("stop")