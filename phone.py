from ppadb.client import Client
from PIL import Image
import numpy
import keyboard

adb = Client(host = '127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no devices')
    quit()

device = devices[0]

image = device.screencap()

with open('screen.png', 'wb') as f:
    f.write(image)

image = Image.open('screen.png')
image = numpy.array(image, dtype=numpy.uint8)

up = 'input tap 540 1012'
lft = 'input tap 308 1246'
rgt = 'input tap 778 1246'
dn = 'input tap 540 1480'

while True:
    if keyboard.is_pressed ("up"):
        device.shell(up)
    if keyboard.is_pressed("left"):
        device.shell(lft)
    if keyboard.is_pressed("right"):
        device.shell(rgt)
    if keyboard.is_pressed("down"):
        device.shell(dn)