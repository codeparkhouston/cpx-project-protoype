import requests
import serial
import time

# These are the site ids of sensors close to the area.
target_site_ids = [1695, 1645, 1640, 1690, 1680, 1600, 1675, 1630, 1685, 575, 590, 595, 585, 545, 1665, 1670]

payload = {
  "regionId": [1],
  "timeSpan": 8,
}
r = requests.post('https://www.harriscountyfws.org/Home/GetSiteRecentData', data = payload)

results = r.json()

# here until line 36 are list comprehensions to loop through the data
# and pull out the current level reading for each sensor of the sites.
sites = [
          {
            'SiteId': feature['properties']['SiteId'],
            'readings': feature['properties']['StreamData'],
          }
          for feature in results['features']
            if feature['properties']['SiteId'] in target_site_ids
        ]

current_readings = [
                      reading
                      for site in sites
                        for reading in site['readings']
                    ]

current_levels = [
                    reading['CurrentLevel']
                    for reading in current_readings
                  ]

# here till line 46 maps the readings to values 0 - 255 relative
# to available readings
level_min = min(current_levels)
level_max = max(current_levels)
level_range = level_max - level_min

ranged_levels = [
                  int((level - level_min) / level_range * 255)
                  for level in current_levels
                ]

# for each mapped level, write into a message format that the CPX will read.
# the format is index:value where index and value are 3 characters long so that
# the CPX can read data as 7 bytes at a time.
message_levels = [
                    '{:03d}'.format(index) + ':' + '{:03d}'.format(ranged_level)
                    for index, ranged_level in enumerate(ranged_levels)
                  ]

# see the result of the data conversion to messages for the CPX
print(message_levels)

# use the pyserial library to open a connection to the USB serial.
# the address/string parameter may need to be changed
# depending on the computer.
ser = serial.Serial('/dev/tty.usbmodem1421')

# loop forever
while True:
  # send a gap message that will make the CPX dim all LEDS
  ser.write(bytes('now:now', encoding='utf-8'))
  for message in message_levels:
    # for each of the converted sensor readings, send a message to
    # the CPX
    ser.write(bytes(message, encoding='utf-8'))
    # wait 0.5 seconds between each message
    time.sleep(0.5)
