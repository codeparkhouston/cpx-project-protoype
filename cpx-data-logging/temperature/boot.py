from adafruit_circuitplayground.express import cpx
import storage

# Storage mode based on slide switch.
# To the left (music note icon) is True, sets the cpx to USB write mode.
# To the right (ear icon) is False, sets the cpx to data logging mode.
storage.remount("/", cpx.switch)