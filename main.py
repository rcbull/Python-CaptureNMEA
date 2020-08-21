import threading

import serial
import time

from configs import *
from utils import *

ser = None


def serial_thread(threadname):
    global ser

    print("Starting serial thread...")

    while True:
        try:

            if ser is None:
                ser = serial.Serial(
                    port=SERIAL_PORT,
                    baudrate=SERIAL_BAUDRATE,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                )

            x = ser.readline().decode('ascii', errors='replace')
            read_nmea(x)

        except Exception as e:
            print("waiting serial conection in ", threadname, e)
            time.sleep(GPS_RECONNECT_IN_SECONDS)
            if ser is not None:
                print('serial connectedl')


if __name__ == '__main__':
    serialThread = threading.Thread(target=serial_thread, args=("serialThread",))
    serialThread.start()
    serialThread.join()
