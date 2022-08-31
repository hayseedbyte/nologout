import time
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.keycode import Keycode
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

x = 0
while x < 1:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
    led.value = True
    time.sleep(0.5)
    led.value = False
    x = 1

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
kbd = Keyboard(usb_hid.devices)


def do_every(period, f, key):
    def g_tick():
        t = time.time()
        while True:
            t += period
            yield max(t - time.time(), 0)

    g = g_tick()
    while True:
        time.sleep(next(g))
        f(key)


def sim_keys(key):
    led.value = True
    kbd.press(key)
    kbd.release(key)
    led.value = False
    time.sleep(0.8)
    led.value = True
    kbd.press(key)
    kbd.release(key)
    led.value = False


do_every(420, sim_keys, Keycode.SCROLL_LOCK)
