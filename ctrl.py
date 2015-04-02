from movement import *

input = raw_input(">_")

while True:
    if input == "w":
        forward()
    elif input == "a":
        left()
    elif input == "s":
        reverse()
    elif input == "d":
        right()
    else:
        stop()

