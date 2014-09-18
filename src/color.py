
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

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "R: %s\t G: %s\tB: %s" % (self.R, self.G, self.B)

    def to_tuple(self):
        """
        return a (R,G,B) tuple representing this colour
        """
        return (self.R, self,G, self.B)