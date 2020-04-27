from pynput.keyboard import Key, Listener, Controller
import serial
from pynput import keyboard
from threading import Thread
import signal

arduino = serial.Serial('/dev/cu.usbserial-1410', 9600, timeout=.1)
interrupted = False
listener_thread = None

def on_press(key):
    # arduino.write(bytes("1", 'utf-8'))
    if key == Key.enter:
        print("frf")
        #arduino.write(bytes("2", 'utf-8'))
    else:
        arduino.write(bytes("1", 'utf-8'))
    # read_serial=arduino.readline()
    # forcedata = int(arduino.readline(),16)
    # serial1[0] = str(forcedata)

def on_release(key):

    print('{0} release'.format(key))
    # arduino.write(bytes("0", 'utf-8'))

    if key == Key.esc:
        # Stop listener
        global interrupted
        interrupted = True
        return False
def signal_handler(signal, frame):
    # example.stop()
    print("interrupted")
    global interrupted
    interrupted = True

def sensorDataRead():
    while not interrupted:
        read_serial=arduino.readline()
        temp = read_serial.decode('utf-8').replace("\n","")
        if(len(temp) != 0):
            print(">>>")
            print(temp)
            num = int(temp,16)
            if num == 5:
                print(">>>>")
                print(num)

                Controller().press(Key.enter)
                Controller().release(Key.enter)




th = Thread(target = sensorDataRead, args = ())
th.start()
# signal.signal(signal.SIGINT, signal_handler)
# Collect events until released

# if not listener_thread:

listener_thread = keyboard.Listener(on_press=on_press, on_release=on_release)
listener_thread.start()
# else:
#     listener_thread.stop()
#     listener_thread = None


# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
