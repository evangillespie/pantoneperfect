import time
from .config import IGNORE_BRIGHT_PIXELS, IGNORE_BRIGHT_THRESHHOLD, PLATFORM
from .config import IMAGE_DIRECTORY, COMPARE_COLOR_SET
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
        get the average color of an image at filepath
        """
        img = Image.open(filepath)
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
            filename = "sky_"+str(int(time.time()))+".jpg"
            self.camera.capture(directory+"/"+filename)
            return directory+"/"+filename
        else:
            "can't take a new picture because you're not on the pi"
            return directory + "/sample.jpg"


    def get_name_from_color_tuple(self, color_tuple):
        """
        return the name of an rgb color tuple

        :param color_tuple: 3 tuple containing R G B values

        :return: string name of that color
        """
        best_name = None
        best_distance = (255*255*3) ** 0.5 # greatest possible distanc

        for name, compare_color in COMPARE_COLOR_SET.iteritems():
            dist = self.get_distance_between_colors(color_tuple, compare_color)

            if dist <= best_distance:
                best_name = name
                best_distance = dist

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

