# CircuitPlaygroundExpress_NeoPixel
 
import time
 
import board
import neopixel

import sys

DIM = (10, 10, 10)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill(DIM)

message = ""
while message is not "end:end":
    # this is how we read messages from the USB serial.
    # we are telling the CPX to read it 7 bytes as at time
    # and to save the messages to the message variable.
    message = sys.stdin.read(7)
    # convert the message back out to an index and value.
    index, value = message.split(':')
    if index.isdigit():
        # set the pixel color for the matching pixel
        pixels[int(index) % len(pixels)] = (int(value), 0, 200)
    else:
        pixels.fill(DIM)
