from os import path

# the size of picture to analyze. bigger makes it more consitent but slower
KMEANS_CONFIG_SIZE = 250

# how big is the hack that biases the color selection to the middle? 0 to turn it off
KMEANS_CONFIG_HACK_FACTOR = 0.007

# Should we ignore all pixels where all values are above a theshhold?
IGNORE_BRIGHT_PIXELS=True

# What is the threshhold for all three colors to ignore the pixels
IGNORE_BRIGHT_THRESHHOLD=220
IGNORE_DARKNESS_THRESHHOLD = 20


# directory in the filesyetem that images are stored in
IMAGE_DIRECTORY = path.join(path.dirname(path.dirname(path.realpath(__file__))), "images")


# Which GPIO pin is the button connected to?
BUTTON_GPIO_PIN = 21

#GUI: PADDING AROUND THE TEXT (ANCHORED IN LOWER LEFT)
GUI_PAD_TEXT_X = 50
GUI_PAD_TEXT_Y = 50


COMPARE_COLOR_SET = {
	'0': (223, 213, 190), #0
	'1': (216, 212, 194), #1 and 2
	'2': (216, 212, 194),
	'3': (215, 211, 215), #3
	'4': (198, 207, 193), #4
	'5': (196, 194, 185), #5
	'6': (188, 196, 191), #6
	'7': (184, 192, 187), #7
	'8': (181, 191, 187), #8
	'9': (185, 204, 195), #9 and 10
	'10': (185, 204, 195), #9 and 10
	'11': (160, 185, 188), #11
	'12': (173, 187, 173), #12
	'13': (164, 188, 191), #13 and 14
	'14': (164, 188, 191),
	'15': (143, 177, 171), #15
	'16': (143, 169, 172), #16
	'17': (129, 158, 168), #17
	'18': (125, 154, 170), #18
	'19': (118, 154, 159), #19
	'20': (120, 159, 168), #20
	'21': (95, 141, 159), #21
	'22': (97, 137, 152), #22
	'23': (90, 128, 147), #23
	'24': (75, 119, 135), #24
	'25': (71, 115, 136), #25
	'26': (94, 120, 143), #26
	'27': (68, 105, 125), #27
	'28': (79, 105, 132), #28
	'29': (52, 101, 127), #29
	'30': (65, 116, 141), #30
	'31': (24, 41, 57), #31
	'32': (52, 101, 127), #32 and 33 and 34
	'33': (52, 101, 127),
	'34': (52, 101, 127),
	'35': (48, 88, 121), #35
	'36': (50, 84, 119), #36
	'37': (57, 87, 117), #37
	'38': (50, 84, 119), #38
	'39': (34, 65, 101), #39
	'40': (56, 79, 107), #40
	'41': (37, 54, 89), #41
	'42': (42, 55, 79), #42
	'43': (47, 54, 84), #43
	'44': (50, 67, 90), #44
	'45': (47, 51, 73), #45 and 46
	'46': (47, 51, 73),
	'47': (38, 49, 69), #47
	'48': (61, 64, 77), #48
	'49': (49, 53, 62), #49
	'50': (46, 50, 56), #50
	'51': (51, 50, 53), #51
	'52': (19, 3, 3), #52
}
