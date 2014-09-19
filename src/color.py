from math import pow, swrt

__author__ = ('evan', )

class PPColor(object):
    """
    class to store a pantone perfect color object
    basically just stored RGB info with some helper methods
    """

    def __init__(self):
        self.R = 0
        self.G = 0
        self.B = 0

    @classmethod
    def create_color(cls, red, green, blue):
        """
        create a PPColor abject

        :param red, green, blue: integer value of that color component

        :return PPColor: PPColor object
        """
        c = cls()
        c.R = red
        c.G = green
        c.B = blue

        return c

    def get_distance(self, other_color_tuple):
        """
        get the distance between this color and another

        :param other_color: the other colour object to compare with

        :return int:
        """
        return sqrt(
            pow(self.R - other_color_tuple[0], 2) +\
            pow(self.G - other_color_tuple[1], 2) +\
            pow(self.B - other_color_tuple[2], 2)
        )

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "R: %s\t G: %s\tB: %s" % (self.R, self.G, self.B)

    def to_tuple(self):
        """
        return a (R,G,B) tuple representing this colour
        """
        return (self.R, self.G, self.B)