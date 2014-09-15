import time
from sys import argv
from PIL import Image

from src.api import PPApi
from src.serial_api import SerialApi

__author__ = ('evan', )

def get_image_color(filepath):
    """
    get the average colour of an image file
    """
    api = PPApi()
    print api.get_image_color(filepath)

def take_picture():
    """
    take a picture and save it in the configured directory
    """
    api = PPApi()
    filename = api.take_picture()

def take_and_analyze_picture():
    """
    take a picture and find the colour
    """
    api = PPApi()
    filename = api.take_picture()
    get_image_color(filename)

def send_serial(r, g, b):
    """
    send an rbg colour to the arduino over serial
    """
    ser = SerialApi()
    ser.send_color(r, g, b)

    time.sleep(1)
    print "done writing"

def picture_to_arduino():
    """
    take a picture and send it's average colour to the arduino over serial
    """
    raise NotImplementedError("no serial yet")

def run(interval):
    raise NotImplementedError("You have not set up the infinite loop yet")

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "get_image_color <path_to_image>"
    print "take_picture"
    print "take_and_analyze_picture"
    print "picture_to_arduino"
    print "send_serial <red> <green> <blue>"
    print "run <update_seconds=60>"

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
            if len(argv) == 3:
                time = int(argv[2])
            else:
                time = 60
                run(time)

    else:
        print_help()