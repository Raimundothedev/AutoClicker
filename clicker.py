import time, pyautogui, threading, keyboard

clicking = False
hotkey = None
cooldown = 0.5

def get_inputs():
    global hotkey, cooldown

    print("Digite a hotkey:")
    hotkey = keyboard.read_key()
    print(f"Hotkey é {hotkey}")

    while True:
        try:
            cooldown = float(input("Digite o intervalo de tempo: "))
        except ValueError:
            print("Digite um número!")
            continue
        break

    return hotkey, cooldown
    

def on_hotkey():
    global clicking
    clicking = not clicking

def click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(cooldown)

def auto_clicker():

    keyboard.add_hotkey(hotkey, on_hotkey)

    thread = threading.Thread(target=click_loop)
    thread.start()

    keyboard.wait()

def start():
    get_inputs()
    auto_clicker()