import time
import os
from sys import argv
from PIL import Image
from os import path
from src.config import PLATFORM, IMAGE_DIRECTORY, COMPARE_COLOR_SET
if PLATFORM == 'pi':
    import RPi.GPIO as GPIO

from src.api import PPApi
from src.gui import PPGui

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
        try:
            filename = api.take_picture()
            color = api.get_image_color(filename)
            name = api.get_name_from_color_tuple(color)
            match_color = COMPARE_COLOR_SET[name]

            print "%s: %s" % (name, color)
            time.sleep(delay)
        except KeyboardInterrupt:
            print "Done."
            break


def run_gui_loop():
    """
    same as run_cli_loop, but uses a gui

    :param delay: time between pictures (seconds)
    """
    gui = PPGui()

    gui.get_root().mainloop()

def generate_images():
    """
    create an image in the output directory for each colour
    available in the set config.COMPARE_COLOR_SET
    """
    print "generating images..."
    directory = path.join(IMAGE_DIRECTORY, "color_swatches")
    size = (300, 300)
    
    for c_tuple in COMPARE_COLOR_SET.values():
        im = Image.new('RGB', size=size, color=c_tuple)
        filename = directory + "/" + str(c_tuple).replace("(", "").replace(")", "").replace(", ", "-") + ".jpg"
        im.save(filename, "JPEG")


def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "generate_images"
    print "get_image_color <path_to_image>"
    print "take_picture"
    print "take_and_analyze_picture"
    print "run_cli_loop"
    print "run_gui_loop"

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
                delay = int(argv[2])
            else:
                delay = 30
            run_cli_loop(delay)
        elif command == 'run_gui_loop':
            run_gui_loop()

        elif command == 'generate_images':
            generate_images()
        
        else:
            print_help()

    else:
        print_help()
