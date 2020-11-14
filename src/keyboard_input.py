from pynput import keyboard
import time


def start_listener():
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            if key == keyboard.Key.esc:
                return False
            print('special key {0} pressed'.format(
                key))

    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False



    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()
    return listener

