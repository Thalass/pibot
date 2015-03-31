from rrb2 import *
import RPi.GPIO as GPIO
import time

rr = RRB2()

def init():
    rr.set_led1(0)
    rr.set_led2(0)
    rr.stop()

def forward(time):
    rr.forward(time)

def left(time):
    rr.left(time)

def right(time):
    rr.right(time)

def stop(time):
    rr.stop(time)

def reverse(time):
    rr.reverse(time)

def main():
    forward(1)
    stop()
    wait(0.5)
    left(1)
    stop()
    wait(0.5)
    right(1)
    stop()
    wait(0.5)
    reverse(1)
    stop()

if "__name__" == "__main__":
    main()


