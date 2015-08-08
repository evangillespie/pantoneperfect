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

def run_cli_loop(delay):
    """
    Run an infinite loop that takes pictures and analyzes them
    then prints the color to the cli

    :param delay: the time between pictures (seconds)
    """

    api = PPApi()
    while True:
        # TODO: implement soft shutdown

        # TODO: should we light an LED to show that the process started?
        filename = api.take_picture()
        color = api.get_image_color(filename)
        print "R:%s G:%s B:%s" % (color[0], color[1], color[2])        
        time.sleep(delay)

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "get_image_color <path_to_image>"
    print "take_picture"
    print "take_and_analyze_picture"
    print "run_cli_loop"

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
        elif command == 'run_cli_loop':
            if len(argv) == 3:
                delay = argv[2]
            else
                delay = 30
                run_cli_loop(delay)

        elif command == 'test':
            test()

    else:
        print_help()
