import pynput
from pynput.keyboard import Key, Listener
keys = []
def on_press(key):
    keys.append(key)
    print(key)
with Listener(on_press = on_press) as Listener:
    Listener.join()
