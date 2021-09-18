# without gpiofrom flask import Flask, render_template, Response
import time

# rpi
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


# ***************    rpi  motor movement code start   ****************

A = 3
B = 5
C = 7
D = 11

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)


def GPIO_setup(a, b, c, d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.002)


def RIGHT_TURN(deg):
    #full_circle = 200.0
    #degree = full_circle / 360 * deg
    degree = (deg)
    print(degree)

    while degree > 0:
        GPIO_setup(1, 0, 0, 0)
        GPIO_setup(1, 1, 0, 0)
        GPIO_setup(0, 1, 0, 0)
        GPIO_setup(0, 1, 1, 0)
        GPIO_setup(0, 0, 1, 0)
        GPIO_setup(0, 0, 1, 1)
        GPIO_setup(0, 0, 0, 1)
        GPIO_setup(1, 0, 0, 1)
        degree -= 1
        if degree == 0:
            break


def LEFT_TURN(deg):
    #full_circle = 200.0
   # degree = full_circle / 360 * deg
    degree = (deg)

    print(degree)

    # while True :
    while degree > 0:
        GPIO_setup(1, 0, 0, 1)
        GPIO_setup(0, 0, 0, 1)
        GPIO_setup(0, 0, 1, 1)
        GPIO_setup(0, 0, 1, 0)
        GPIO_setup(0, 1, 1, 0)
        GPIO_setup(0, 1, 0, 0)
        GPIO_setup(1, 1, 0, 0)
        GPIO_setup(1, 0, 0, 0)
        degree -= 1
        if degree == 0:
            break
        # break
        # degree -=1


def NO_TURN(deg):
    GPIO_setup(0, 0, 0, 0)

def move_stepper(section):
    if section == "A":
        # arduino.write(notmatch)
        RIGHT_TURN(5)
        GPIO_setup(0, 0, 0, 0)

    if section == "B":
        # arduino.write(matching)
        RIGHT_TURN(3)
        GPIO_setup(0, 0, 0, 0)

    if section == "D":
        # arduino.write(notmatch)
        LEFT_TURN(3)
        GPIO_setup(0, 0, 0, 0)

    elif section == "E":
        LEFT_TURN(5)
        GPIO_setup(0, 0, 0, 0)

    else:
        NO_TURN(0)
        GPIO_setup(0, 0, 0, 0)

