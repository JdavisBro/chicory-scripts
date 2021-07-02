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

levels = []

for i in range(34):
    with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata","r") as f:
        lines = f.readlines()
    line4 = json.loads(lines[3])
    line4["progress"] = i
    lines[3] = json.dumps(line4) + "\n"
    with open("/home/jdavis/.local/share/Steam/steamapps/compatdata/1123450/pfx/drive_c/users/steamuser/Local Settings/Application Data/paintdog/save/_playdata","w") as f:
        f.writelines(lines)
    mouse.position = continue_button
    time.sleep(0.1)
    mouse.press(Mouse.Button.left)
    time.sleep(0.1)
    mouse.release(Mouse.Button.left)
    mouse.position = (1920,0)
    time.sleep(5)
    im = ImageGrab.grab()
    im.save(f"screenshots/{i}.png")
    keyboard.tap(Keyboard.Key.esc)
    time.sleep(0.2)
    for _ in range(4):
        keyboard.tap(Keyboard.Key.down)
        time.sleep(0.2)
    keyboard.tap(Keyboard.Key.enter)
    time.sleep(3)
