import time
import threading
import keyboard
import pyautogui

from config import Config


clicking = False
running = False


def on_hotkey():
    global clicking

    clicking = not clicking
    print(f"Clicking: {clicking}")


def set_hotkey():
    global clicking

    clicking = False

    print("Pressione a nova hotkey...")
    new_hotkey = keyboard.read_key()

    keyboard.remove_all_hotkeys()

    Config.hotkey = new_hotkey

    keyboard.add_hotkey(Config.hotkey, on_hotkey)

    print(f"Nova hotkey: {Config.hotkey}")


def click_loop():
    global running

    while running:
        if clicking:
            pyautogui.click()
            time.sleep(Config.interval)
        else:
            time.sleep(0.01)


def start():
    global running

    if running:
        return

    running = True

    keyboard.add_hotkey(Config.hotkey, on_hotkey)

    thread = threading.Thread(target=click_loop, daemon=True)
    thread.start()


def stop():
    global running, clicking

    running = False
    clicking = False

    keyboard.remove_all_hotkeys()