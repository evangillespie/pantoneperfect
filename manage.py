import time
from sys import argv
from PIL import Image
import RPi.GPIO as GPIO

from src.api import PPApi
from src.serial_api import SerialApi

__author__ = ('evan', )

def get_image_color(filepath):
    """
    get the average colour of an image file
    """
    api = PPApi()
    color = api.get_image_color(filepath)
    return color

def take_picture(api = None):
    """
    take a picture and save it in the configured directory
    """
    if api == None:
        api = PPApi()
    filename = api.take_picture()

def take_and_analyze_picture(api = None):
    """
    take a picture and find the colour
    """
    if api == None:
        api = PPApi()
    filename = api.take_picture(api)
    color = get_image_color(filename)
    return color

def send_serial(r, g, b):
    """
    send an rbg colour to the arduino over serial
    """
    #make sure that r,g,b are ints
    r = int(r)
    g = int(g)
    b = int(b)
            
    ser = SerialApi()
    ser.send_color(r, g, b)

def picture_to_arduino():
    """
    take a picture and send it's average colour to the arduino over serial
    """
    color = take_and_analyze_picture()
    print color
    send_serial(color[0], color[1], color[2])

def run():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.IN)
    api = PPApi()
    serial_api = SerialApi()
    while True:
        # TODO: implement soft shutdown

        input_value = GPIO.input(24)
        if input_value == True:
            # TODO: should we light an LED to show that the process started?
            filename = api.take_picture()
            color = api.get_image_color(filename)
            r = color[0]
            g = color[1]
            b = color[2]
            serial_api.send_color(r, g, b)

        time.sleep(0.01)

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "get_image_color <path_to_image>"
    print "take_picture"
    print "take_and_analyze_picture"
    print "picture_to_arduino"
    print "send_serial <red> <green> <blue>"
    print "run"

if __name__ == '__main__':
    if len(argv) >= 2:
        command = argv[1]
        if command == 'get_image_color' or command == 'get_image_colour':
            if len(argv) == 3:
                get_image_color(argv[2])
            else: print_help()
        elif command == 'take_picture':
            take_picture()
        elif command == 'take_and_analyze_picture':
            take_and_analyze_picture()
        elif command == "picture_to_arduino":
            picture_to_arduino()
        elif command == "send_serial":
            if len(argv) == 5:
                send_serial(argv[2], argv[3], argv[4])
            else:
                print_help()
        elif command == 'run':
                run()
        elif command == 'test':
            test()

    else:
        print_help()
