import numpy as np
import operator  # import modul add
ethernet_devices = [1, [7], [2], [8374163], [84302738]]
usb_devices = [1, [7], [1], [2314567], [0]]

# the long way
print('----------the long way---------')
all_devices = [
    ethernet_devices[0] + usb_devices[0],
    ethernet_devices[1] + usb_devices[1],
    ethernet_devices[2] + usb_devices[2],
    ethernet_devices[3] + usb_devices[3],
    ethernet_devices[4] + usb_devices[4]
]
print(all_devices)

# some comprehension magic
print('------------------some comprehension magic----------')
all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]
print(all_devices)

# let's use maps
print('---------------lets you map---------')
# ham map gom function va cac doi so
all_devices = list(map(operator.add, ethernet_devices, usb_devices))
print(all_devices)

# We can't forget our favorite computation library
print('---------------use numpy-------------')
all_devices = np.add(ethernet_devices, usb_devices)
print(all_devices)
