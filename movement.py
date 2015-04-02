from rrb2 import *
import RPi.GPIO as GPIO
from time import sleep

rr = RRB2()
print "setup complete"

def init():
    rr.set_led1(1)
    rr.set_led2(0)
    rr.stop()
    print "initialized"

def forward():
    rr.forward(0)
    print "forward"

def left():
    rr.left(0)
    print "left"

def right():
    rr.right(0)
    print "right"

def reverse():
    rr.reverse(0)
    print "reverse" 

def stop():
    rr.stop()
    print "stop"

def main():
    pass

if "__name__" == "__main__":
    main()


