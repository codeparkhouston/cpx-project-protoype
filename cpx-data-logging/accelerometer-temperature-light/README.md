This is code that helps us program the CPX to log sensor data from the board to a file.  There are two code files -- `boot.py` and `code.py`.  `data.txt` is some previously logged data as an example for what will be recorded.

# `boot.py`

When CPX starts up, it runs the code in the `boot.py` file.  The code programs the CPX to use the slide switch to determine whether the CPX is in USB write mode -- for programming -- or in self-writing mode -- for data logging.

# `code.py`

The code in this file is run after the `boot.py` code runs.

The code in this file controls one of two things: reading data from sensors and writing information to a file.

To talk through this code as a class, it would be helpful to start first with the familar concept of reading data from sensors:

```py
import time
from adafruit_circuitplayground.express import cpx

# Forever,
while True:

    x, y, z = cpx.acceleration
    temperature = cpx.temperature
    light = cpx.light

    # Wait 1 second before collecting data again.
    time.sleep(1)
```

To make the data collection more clear, we can progress to printing the data and even taking advantage of Mu's plotter:

```py
import time
from adafruit_circuitplayground.express import cpx

# Forever,
while True:

    x, y, z = cpx.acceleration
    temperature = cpx.temperature
    light = cpx.light

    # Print the data so we can see the data
    # By printing the data as a tuple, Mu will plot it for realtime line graphs.
    print((x, y, z, temperature, light))

    # Wait 1 second before collecting data again.
    time.sleep(1)
```

Experiment with the CPX and let students observe the changes in the realtime plotter.

Next, we can replace the logging code with code that combines the different sensor readings together into a line of text.  We print each line of code to see what that will look like.

```py
import time
from adafruit_circuitplayground.express import cpx

# Forever,
while True:

    x, y, z = cpx.acceleration
    temperature = cpx.temperature
    light = cpx.light

    # This line takes the sensor data and puts it in a format where
    # the numbers will be separated by commas like so:
    # x, y, z, temperature, light
    data = '{:f}, {:f}, {:f}, {:f}, {:f}\n'.format(x, y, z, temperature, light)
    print(data)

    # Wait 1 second before collecting data again.
    time.sleep(1)
```

The rest of the code we add will be related to data logging.  Sometimes code can fail.  We've seen it before with error messages when we mispell the code.  We can use something called error handling to help as we prepare to add writing the data to files.

In Python, we use `try:` and `except:`

```py
import time
from adafruit_circuitplayground.express import cpx

# Sometimes, our cpx cannot always do what we ask.
# Here we ask our cpx board to try something and if it
# cannot do it, it will run the code in the except block
# of code.
try:
    # Forever,
    while True:

        x, y, z = cpx.acceleration
        temperature = cpx.temperature
        light = cpx.light

        # This line takes the sensor data and puts it in a format where
        # the numbers will be separated by commas like so:
        # x, y, z, temperature, light
        data = '{:f}, {:f}, {:f}, {:f}, {:f}\n'.format(x, y, z, temperature, light)

        # Wait 1 second before collecting data again.
        time.sleep(1)
# This code will run if the code in the try block has errors.
# Why the code in the try block cannot run will be remembered
# as the variable named error.
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
```

Next, we can add code for writing to a file.  In Python, we open a "stream" to a file, which is a computer science construct that is like a conveyor belt.  We can place information on the stream and it will be transported to the file.  The stream we are opening to the file is in the mode "a", which is short for append only, meaning this will only add to the file and never erase.


```py
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

            x, y, z = cpx.acceleration
            temperature = cpx.temperature
            light = cpx.light
            
            # We can visualize data live here using the pixels as we'd like.
            # This could cause the cpx to run out of batteries though.


            # This line takes the sensor data and puts it in a format where
            # the numbers will be separated by commas like so:
            # x, y, z, temperature, light
            data = '{:f}, {:f}, {:f}, {:f}, {:f}\n'.format(x, y, z, temperature, light)
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
```