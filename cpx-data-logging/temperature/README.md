Same as https://learn.adafruit.com/data-logging-with-feather-and-circuitpython/circuitpython-code but using cpx library so we can write less code.

The tutorial uses lower level libraries `board` and `digitalio` to toggle storage

```py
import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D7)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

storage.remount("/", switch.value)
```

Using the cpx library, we can do the same thing, like this:

```py
from adafruit_circuitplayground.express import cpx
import storage

storage.remount("/", cpx.switch)
```