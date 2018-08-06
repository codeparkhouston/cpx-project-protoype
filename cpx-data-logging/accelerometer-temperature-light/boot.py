# Import the code that lets us read input and set output
# to our cpx.
from adafruit_circuitplayground.express import cpx

# Import storage library so we can use it to
# change the storage mode of our cpx board.
# 
# Our cpx board is usually like a USB drive --
# we can write information or code to it over USB.
# To save information that cpx senses to itself,
# the storage mode will need to be set to data logging mode.
import storage

# Storage mode based on slide switch.
# To the left (music note icon) is True, sets the cpx to USB write mode.
# To the right (ear icon) is False, sets the cpx to data logging mode.
storage.remount("/", cpx.switch)