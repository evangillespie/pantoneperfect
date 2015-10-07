import time
from os import path
from random import choice
from .config import IGNORE_BRIGHT_PIXELS, IGNORE_BRIGHT_THRESHHOLD
from .config import IMAGE_DIRECTORY, COMPARE_COLOR_SET
from .platform import PLATFORM
from PIL import Image
if PLATFORM == 'pi':
    import picamera


__author__ = ('Evan Gillespie', )


class PPApi(object):
    """
    class to handle requests to the pantone perfect application
    """

    def __init__(self):
        if PLATFORM == 'pi':
            self.camera = picamera.PiCamera()
            self.camera.resolution = (640, 480)
        else:
            pass

    def get_image_color(self, filepath):
        """
        get the color of the sky in an image

        :param filepath: path to the image we are finding the color of

        :return: (R, G, B) tuple
        """
        return self.get_most_common_image_color(filepath)


    def get_most_frequent_image_color(self, filepath):
        """
        get the most frequently used pixel color by comparing 
        each pixel to the possible colors
        """
        with Image.open(filepath) as img:
            w, h = img.size
            max_count = 0
            color = None
            counts = {}
            for count, c in img.getcolors(w*h):
                if IGNORE_BRIGHT_PIXELS:
                    if c[0] >= IGNORE_BRIGHT_THRESHHOLD and \
                        c[1] >= IGNORE_BRIGHT_THRESHHOLD and \
                        c[2] >= IGNORE_BRIGHT_THRESHHOLD:
                        continue

                    n = self.get_name_from_color_tuple(c, max_distance=50)
                    if n == None:
                        continue    # too far from named colors
                    if n in counts:
                        counts[n] += count
                    else:
                        counts[n] = count

            max = 0
            max_color_name = None
            for color_name, num in counts.iteritems():
                if num > max:
                    max_color_name = color_name
                    max = num

            return COMPARE_COLOR_SET[max_color_name]


    def get_most_common_image_color(self, filepath):
        """
        get the most common pixel color from an image
        """
        with Image.open(filepath) as img:
            w, h = img.size
            max_count = 0
            color = None
            for count, c in img.getcolors(w*h): # max colors is a different color in each pixel
                if IGNORE_BRIGHT_PIXELS:
                    if c[0] >= IGNORE_BRIGHT_THRESHHOLD and \
                        c[1] >= IGNORE_BRIGHT_THRESHHOLD and \
                        c[2] >= IGNORE_BRIGHT_THRESHHOLD:
                        continue

                if count > max_count:
                    color = c

        return c


    def get_average_image_color(self, filepath):
        """
        XXX: old way of finding dominant image color
        get the average color of an image at filepath
        """
        with Image.open(filepath) as img:
            pixel_sum = {'red':0, 'green':0, 'blue':0}
            pixel_count = 0
            for r,g,b in img.getdata():
                if IGNORE_BRIGHT_PIXELS:
                    if r >= IGNORE_BRIGHT_THRESHHOLD and \
                        g >= IGNORE_BRIGHT_THRESHHOLD and \
                        b >= IGNORE_BRIGHT_THRESHHOLD:
                        continue

                pixel_sum['red'] += r
                pixel_sum['green'] += g
                pixel_sum['blue'] += b
                pixel_count += 1

            r_avg = int(pixel_sum['red'] / pixel_count)
            g_avg = int(pixel_sum['green'] / pixel_count)
            b_avg = int(pixel_sum['blue'] / pixel_count)

        return (r_avg, g_avg, b_avg)

    def take_picture(self):
        """
        take a picture and save it in the configured place

        :return string: filename
        """
        directory = IMAGE_DIRECTORY
        if PLATFORM == 'pi':
            directory = path.join(IMAGE_DIRECTORY, "camera")
            filename = "sky_"+str(int(time.time()))+".jpg"
            self.camera.capture(directory+"/"+filename)
            return path.join(directory,filename)
        else:
            # can't take a new picture because you're not on the pi
            return path.join(directory,"sample%d.jpg" % choice(range(4)))


    def get_name_from_color_tuple(self, color_tuple, max_distance=None):
        """
        return the name of an rgb color tuple

        :param color_tuple: 3 tuple containing R G B values
        :param max_distance: te maximum distance between the named color and color_tuple

        :return: string name of that color. None if max_distance is exceeded
        """
        best_name = None
        best_distance = (255*255*3) ** 0.5 # greatest possible distanc

        for name, compare_color in COMPARE_COLOR_SET.iteritems():
            dist = self.get_distance_between_colors(color_tuple, compare_color)

            if dist <= best_distance:
                best_name = name
                best_distance = dist

        if max_distance != None:
            if best_distance > max_distance:
                return None

        return best_name


    def get_distance_between_colors(self, color1, color2):
        """
        get the euclidean distance between two color tuples

        :param color1: first color to compare
        :param color2: second color to compare

        :return: distance between them
        """
        dist = ((color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)**0.5

        return dist


    def print_color(self, name, color, filename):
        """
        print information about the color
        """
        print "%s: %s\t(%s)" % (name, color, path.basename(filename))