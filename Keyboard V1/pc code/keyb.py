from pynput.keyboard import Key, Listener
import serial
from pynput import keyboard
from threading import Thread
import signal

arduino = serial.Serial('/dev/cu.usbserial-1410', 9600, timeout=.1)
listener_thread = None

def on_press(key):
    if key == Key.enter:

        arduino.write(bytes("2", 'utf-8'))
    else:
        arduino.write(bytes("1", 'utf-8'))

def on_release(key):

    print('{0} release'.format(key))

    if key == Key.esc:
        # Stop listener
        global interrupted
        interrupted = True
        return False

listener_thread = keyboard.Listener(on_press=on_press, on_release=on_release)
listener_thread.start()
