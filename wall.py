import ctypes
import os
import time as t
import keyboard as k
import time as t
a = 1

def set_wallpaper(image_path):
    if os.path.exists(image_path):
        abs_path = os.path.abspath(image_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
        print(f"{image_path}")
    else:
        print(f"{image_path} error")
while True:
    while a <= 1133:
        set_wallpaper(f"frames/frame_{a}.jpg")
        a = a + 1
        t.sleep(0.04)
    a = 0
