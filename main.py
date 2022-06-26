import time
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.keycode import Keycode

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
    kbd.press(key)
    # time.sleep(0.3)
    kbd.release(key)
    print("pressed1")
    time.sleep(0.8)
    kbd.press(key)
    # time.sleep(0.3)
    kbd.release(key)
    print("pressed2")


do_every(420, sim_keys, Keycode.SCROLL_LOCK)
