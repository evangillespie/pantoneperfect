import time
from .color import PPColor
from .config import IGNORE_BRIGHT_PIXELS, IGNORE_BRIGHT_THRESHHOLD, IMAGE_DIRECTORY, COMPARE_COLOR, COMPARE_COLOR_SET
from PIL import Image
import picamera

__author__ = ('evan', )

class PPApi(object):
    """
    class to handle requests to the pantone perfect application
    """

    def __init__(self):
        self.camera = picamera.PiCamera()

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

        color = PPColor.create_color(r_avg, g_avg, b_avg)
        if COMPARE_COLOR:
            min_distance = 255*255*3    # some impossibly huge distance
            best_match = None
            for compare_color_tuple in COMPARE_COLOR_SET:
                distance = color.get_distance(compare_color_tuple)
                if ( not best_match ) or ( distance < min_distance ):
                    best_match = PPColor.create_color(compare_color_tuple[0], compare_color_tuple[1], compare_color_tuple[2])
                    min_distance = distance
            return best_match.to_tuple()
        else:
            return color.to_tuple()

    def take_picture(self):
        """
        take a picture and save it in the configured place

        :return string: filename
        """
        
        filename = "sky_"+str(int(time.time()))+".jpg"
        directory = IMAGE_DIRECTORY
        
        self.camera.capture(directory+"/"+filename)
        return directory+"/"+filename

        
