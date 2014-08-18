
from sys import argv

from src.api import PPApi

__author__ = ('evan', )

def get_image_color(filepath):
    """
    get the average colour of an image file
    """
    api = PPApi()
    print api.get_image_color(filepath)

def take_picture():
    raise NotImplementedError("You have not set up picture taking yet")

def run(interval):
    raise NotImplementedError("You have not set up the infinite loop yet")

def print_help():
    print "USAGE: %s <command>" % argv[0]
    print "COMMANDS:"
    print "get_image_color <path_to_image>"
    print "take_picture"
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
        elif command == 'run':
            if len(argv) == 3:
                time = int(argv[2])
            else:
                time = 60
                run(time)

    else:
        print_help()