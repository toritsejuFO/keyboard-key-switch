from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

def on_press(key):
    if key == Key.alt_r:
        keyboard.press('(')
        keyboard.release('(')
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        return

def on_release(key):
    return

    if key == key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
