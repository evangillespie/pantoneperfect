# Should we ignore all pixels where all values are above a theshhold?
IGNORE_BRIGHT_PIXELS=True

# What is the threshhold for all three colors to ignore the pixels
IGNORE_BRIGHT_THRESHHOLD=230

# directory in the filesyetem that images are stored in
IMAGE_DIRECTORY = '/home/pi/pantoneperfect/images'

# where to look for the arduino on serial
SERIAL_DEVICE = '/dev/ttyACM0'
SERIAL_DEVICE2 = '/dev/ttyACM1'

# Should we compare the colour to one of a pre-defined set?
COMPARE_COLOR=True

COMPARE_COLOR_SET = [
	(255, 255, 255),
	(255, 0, 0),
	(0, 255, 0),
	(0, 0, 255),
	(0, 0, 0)
]
