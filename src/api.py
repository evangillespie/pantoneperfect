import time
from .color import PPColor
from .config import IGNORE_BRIGHT_PIXELS, IGNORE_BRIGHT_THRESHHOLD, IMAGE_DIRECTORY
from PIL import Image

# sudo apt-get install python-picamera
import picamera

__author__ = ('evan', )

class PPApi(object):
    """
    class to handle requests to the pantone perfect application
    """

    def __init__(self):
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

        return PPColor.create_color(r_avg, g_avg, b_avg)

    def take_picture(self):
        """
        take a picture and save it in the configured place

        :return string: filename
        """
        filename = "sky_"+str(int(time.time()))+".jpg"
        directory = IMAGE_DIRECTORY
        camera = picamera.PiCamera()
        camera.capture(directory+"/"+filename)
        return directory+"/"+filename

        
