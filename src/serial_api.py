from .config import SERIAL_DEVICE

__author__ = ('evan', )

class SerialApi(object):
    """
    class to handle serial communication with the arduino
    """

    def __init__(self):
        pass
        # TODO: connect over serial

    def send_color(self, r, g, b):
    	"""
    	send a colour string over the serial connection to the arduino

    	:param r: red component 0-255
    	:param g: green
    	:param b: blue
    	"""
    	# make sure the components are integers
    	r = int(r)
    	g = int(g)
    	b = int(b)

    	if r > 255 or r < 0:
    		raise Exception("red component out of range: %s" % r)
    	if g > 255 or g < 0:
    		raise Exception("green component out of range: %s" % g)
    	if b > 255 or b < 0:
    		raise Exception("blue component out of range: %s" % b)
    		
    	ser_str = '%03d%03d%03d' % (r,g,b)
    	
    	# TODO: send the serial string
