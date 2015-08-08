import time
import os
from sys import argv
from PIL import Image
import RPi.GPIO as GPIO

from src.api import PPApi

__author__ = ('evan', )

def get_image_color(filepath, printout = False):
    """
    get the average colour of an image file
    """
    api = PPApi()
    color = api.get_image_color(filepath)
    if printout:
        print color
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
    filename = api.take_picture()
    color = api.get_image_color(filename)
    print color
    return color

def run():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(7, GPIO.IN)
    api = PPApi()
    while True:
        # TODO: implement soft shutdown

        input_value = GPIO.input(18)
        shutdown = GPIO.input(7)
        if input_value == True:
            # TODO: should we light an LED to show that the process started?
            filename = api.take_picture()
            color = api.get_image_color(filename)
            r = color[0]
            g = color[1]
            b = color[2]
            # @TODO: do something with the color
        if shutdown == True:
            os.system("sudo shutdown -h now")
            break

        time.sleep(0.01)

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "get_image_color <path_to_image>"
    print "take_picture"
    print "take_and_analyze_picture"
    print "run"

if __name__ == '__main__':
    if len(argv) >= 2:
        command = argv[1]
        if command == 'get_image_color' or command == 'get_image_colour':
            if len(argv) == 3:
                get_image_color(argv[2], printout=True)
            else: print_help()
        elif command == 'take_picture':
            take_picture()
        elif command == 'take_and_analyze_picture':
            take_and_analyze_picture()
        elif command == 'run':
                run()
        elif command == 'test':
            test()

    else:
        print_help()
