
from .color import PPColor
from PIL import Image

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
            pixel_sum['red'] += r
            pixel_sum['green'] += g
            pixel_sum['blue'] += b
            pixel_count += 1

        r_avg = int(pixel_sum['red'] / pixel_count)
        g_avg = int(pixel_sum['green'] / pixel_count)
        b_avg = int(pixel_sum['blue'] / pixel_count)

        return PPColor.create_color(r_avg, g_avg, b_avg)