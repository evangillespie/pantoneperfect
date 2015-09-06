from Tkinter import *
from random import choice
from .platform import PLATFORM
from .config import COMPARE_COLOR_SET
from .api import PPApi


__author__ = ("Evan Gillespie",)


class PPGui(object):
	"""
	class to create and handle the gui for pantone perfect
	"""

	def __init__(self):
		"""
		initialize the gui
		"""
		self.api = PPApi()

		self.root = Tk()

		# make the root widget fullscreen
		if PLATFORM == 'pi':
			w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
			self.root.overrideredirect(1)
		else:
			w = 250
			h = 250
		self.root.geometry("%dx%d+0+0" % (w, h))

		self.label = Label(
			self.root,
			text="",
			# hex color string. This code formats it correctly: '#%02x%02x%02x' % (64, 204, 208)
			bg='#555555',
			fg='#FFFFFF',
			anchor=SW,
			font=("Helvetica", 30),
		)
		self.label.bind("<Button-1>", self.take_picture_and_analyze) 
		self.label.pack(fill=BOTH, expand=1)


	def take_picture_and_analyze(self, event):

		filename = self.api.take_picture()
		color = self.api.get_image_color(filename)
		name = self.api.get_name_from_color_tuple(color)
		display_color = COMPARE_COLOR_SET[name]

		self.api.print_color(name, color, filename)

		# @TODO: should I display the color of the image or the color of the closest match?
		bgc = '#%02x%02x%02x' % (display_color[0], display_color[1], display_color[2])

		# All this logic comes from https://24ways.org/2010/calculating-color-contrast/
		yiq = ((display_color[0]*299)+(display_color[1]*587)+(display_color[2]*114))/1000;
		if yiq >= 128:
			fgc = "#000000"
		else:
			fgc = "#FFFFFF"

		self.label.config(bg=bgc, fg=fgc, text=name)


	def get_root(self):
		return self.root