import os
import time
import json
from pynput import mouse as Mouse
from pynput import keyboard as Keyboard
from PIL import ImageGrab

time.sleep(5)

continue_button = (1741, 808)

mouse = Mouse.Controller()
keyboard = Keyboard.Controller()

levels = os.listdir("failures/get_shots_myself")

for level in levels:
    level = level[:-4]
    level = level.split("_")
    with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata","r") as f:
        lines = f.readlines()
    lines[0] = level[1] + " \n"
    lines[1] = level[2] + " \n"
    lines[2] = level[0] + " \n"
    lines[4] = "70.8009 \n"
    lines[5] = "105.026 \n"
    with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata","w") as f:
        f.writelines(lines)
    mouse.position = continue_button
    time.sleep(0.1)
    mouse.press(Mouse.Button.left)
    time.sleep(0.1)
    mouse.release(Mouse.Button.left)
    time.sleep(0.7)
    keyboard.tap("r")
    time.sleep(2)
    def on_press(key):
        if key == Keyboard.Key.shift_r:
            raise ValueError
    with Keyboard.Listener(on_press=on_press) as l:
        try:
            l.join()
        except:
            pass
    mouse.position = (1920,0)
    im = ImageGrab.grab()
    im.save(f"screenshots/{'_'.join(level)}.png")
    keyboard.tap(Keyboard.Key.esc)
    time.sleep(0.2)
    for _ in range(4):
        keyboard.tap(Keyboard.Key.down)
        time.sleep(0.2)
    keyboard.tap(Keyboard.Key.enter)
    time.sleep(3)
