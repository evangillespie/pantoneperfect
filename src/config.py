
# what platform is this being run on right now?
PLATFORM = 'pc'


# Should we ignore all pixels where all values are above a theshhold?
IGNORE_BRIGHT_PIXELS=True


# What is the threshhold for all three colors to ignore the pixels
IGNORE_BRIGHT_THRESHHOLD=230


# directory in the filesyetem that images are stored in
if PLATFORM == "pi":
	IMAGE_DIRECTORY = '/home/pi/pantoneperfect/images'
elif PLATFORM == "pc":
	IMAGE_DIRECTORY = '/Users/evan/Documents/programs/pantoneperfect/images'


# Should we compare the colour to one of a pre-defined set?
COMPARE_COLOR=True


COMPARE_COLOR_SET = [
	(223, 213, 190), #0
	(216, 212, 194), #1 and 2
	(215, 211, 215), #3
	(198, 207, 193), #4
	(196, 194, 185), #5
	(188, 196, 191), #6
	(184, 192, 187), #7
	(181, 191, 187), #8
	(185, 204, 195), #9 and 10
	(160, 185, 188), #11
	(173, 187, 173), #12
	(164, 188, 191), #13 and 14
	(143, 177, 171), #15
	(143, 169, 172), #16
	(129, 158, 168), #17
	(125, 154, 170), #18
	(118, 154, 159), #19
	(120, 159, 168), #20
	(95, 141, 159), #21
	(97, 137, 152), #22
	(90, 128, 147), #23
	(75, 119, 135), #24
	(71, 115, 136), #25
	(94, 120, 143), #26
	(68, 105, 125), #27
	(79, 105, 132), #28
	(52, 101, 127), #29
	(65, 116, 141), #30
	(24, 41, 57), #31
	(52, 101, 127), #32 and 33 and 34
	(48, 88, 121), #35
	(50, 84, 119), #36
	(57, 87, 117), #37
	(50, 84, 119), #38
	(34, 65, 101), #39
	(56, 79, 107), #40
	(37, 54, 89), #41
	(42, 55, 79), #42
	(47, 54, 84), #43
	(50, 67, 90), #44
	(47, 51, 73), #45 and 46
	(38, 49, 69), #47
	(61, 64, 77), #48
	(49, 53, 62), #49
	(46, 50, 56), #50
	(51, 50, 53), #51
	(19, 3, 3), #52
	(119, 201, 199), # Middle Grey Pantone 420 C
]
