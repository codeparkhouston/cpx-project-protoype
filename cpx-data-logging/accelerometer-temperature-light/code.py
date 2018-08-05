import time
from adafruit_circuitplayground.express import cpx

try:
    with open("/data.txt", "a") as fp:
        while True:
            x, y, z = cpx.acceleration
            temperature = cpx.temperature
            light = cpx.light
            
            # we can visualize data live here using the pixels as we'd like.



            # writing data to the file
            data = '{:f}, {:f}, {:f}, {:f}, {:f}\n'.format(x, y, z, temperature, light)
            fp.write(data)
            fp.flush()

            time.sleep(1)
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        cpx.red_led = not cpx.red_led

        time.sleep(delay)
