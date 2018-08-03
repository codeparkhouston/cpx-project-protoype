import time
from adafruit_circuitplayground.express import cpx

try:
    with open("/temperature.txt", "a") as fp:
        while True:
            temp = cpx.temperature
            
            # do the C-to-F conversion here if you would like
            fp.write('{0:f}\n'.format(temp))
            fp.flush()
            cpx.red_led = not cpx.red_led
            cpx.pixels[0] = (100, 200, 300)
            time.sleep(1)
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        cpx.red_led = not cpx.red_led
        cpx.pixels[0] = (0, 0, 255)

        time.sleep(delay)