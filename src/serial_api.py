from .config import SERIAL_DEVICE, SERIAL_DEVICE2
import sys
import serial
from time import sleep

__author__ = ('evan', )

class SerialApi(object):
    """
    class to handle serial communication with the arduino
    """

    def __init__(self):
        self.ser = None
        try:
            self.ser = serial.Serial(SERIAL_DEVICE, 9600, timeout=5.0) # 5 second read timeout.
        except serial.serialutil.SerialException:
            try:
                self.ser = serial.Serial(SERIAL_DEVICE2, 9600)
            except serial.serialutil.SerialException:
                print "cant find arduino. Exiting"
                sys.exit()

        sleep(1)

    def send_color(self, r, g, b):
        """
        send a colour string over the serial connection to the arduino

        :param r: red component 0-255
        :param g: green
        :param b: blue
        """
        # make double sure the components are integers
        r = int(r)
        g = int(g)
        b = int(b)

        if r > 255 or r < 0:
            raise Exception("red component out of range: %s" % r)
        if g > 255 or g < 0:
            raise Exception("green component out of range: %s" % g)
        if b > 255 or b < 0:
            raise Exception("blue component out of range: %s" % b)

        self.ser.write(chr(r))
        self.ser.write(chr(g))
        self.ser.write(chr(b))
        feedback = self.ser.read()
