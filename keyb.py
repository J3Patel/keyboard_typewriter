from pynput.keyboard import Key, Listener
import serial
import keyboard

arduino = serial.Serial('/dev/cu.usbserial-1410', 115200, timeout=.1)

def on_press(key):
    # arduino.write(bytes("1", 'utf-8'))
    if key == Key.enter:
        arduino.write(bytes("2", 'utf-8'))
    else:
        arduino.write(bytes("1", 'utf-8'))
    # read_serial=arduino.readline()
    # forcedata = int(arduino.readline(),16)
    # serial1[0] = str(forcedata)

def on_release(key):

    print('{0} release'.format(key))
    # arduino.write(bytes("0", 'utf-8'))

    # if key == Key.esc:
    #     # Stop listener
    #     return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
