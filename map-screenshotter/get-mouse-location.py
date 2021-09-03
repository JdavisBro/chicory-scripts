from pynput.keyboard import Listener
from pynput.mouse import Controller

mouse = Controller()

def on_press(key):
    print(mouse.position)

def on_release(key):
    pass

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()