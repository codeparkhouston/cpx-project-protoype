import time
from adafruit_circuitplayground.express import cpx

# Sometimes, our cpx cannot always do what we ask.
# Here we ask our cpx board to try something and if it
# cannot do it, it will run the code in the except block
# of code.
# 
# In this case, we will ask the cpx to try to log data
# to a file.  This will only run if the cpx board is in data logging
# mode.  In USB write mode, the cpx will run the code in the
# except block to show that it is erroring.
try:
    # We ask cpx to open a stream to a file named data.txt.
    # The stream is remembered by our code as the variable data_log.
    # This file is opened in "appending" mode, which means we can only add
    # to the file.
    with open("/data.txt", "a") as data_log:

        # Forever,
        while True:

            # Data we want to collect saved to variables here.


            
            # We can visualize data live here using the pixels as we'd like.
            # This could cause the cpx to run out of batteries though.



            # This line takes the sensor data and puts it in a format where
            # the numbers will be separated by commas like so:
            # x, y, z, temperature, light
            data = # how we want to format the data here.


            # This writes the data to our data_log stream.
            data_log.write(data)
            # 
            data_log.flush()

            # We can indicate status of data logging here.

            # Wait 1 second before collecting data again.
            time.sleep(1)


# This code will run if the cpx is not in data logging mode or
# if the cpx runs out of space.  Why the code in the try block
# cannot run will be remembered as the variable named error.
except OSError as error:

    delay = 0.5

    # Error code of 28 means the cpx is out of space.
    # The delay variable is shorter if the cpx runs out of space.
    if error.args[0] == 28:
        delay = 0.25

    # Forever
    while True:

        # not cpx.red_led will switch between True and False,
        # causing the red led to blink
        cpx.red_led = not cpx.red_led
        # Sleep inbetween red led on and off.
        # The delay variable is 0.5 for most errors and
        # 0.25 for out of space error.
        # This means that the red led will blink at 0.25 seconds
        # when the cpx is out of space and at 0.5 seconds
        # for all other errors.
        time.sleep(delay)
