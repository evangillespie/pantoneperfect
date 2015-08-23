from Tkinter import *
from random import choice


__author__ = ("Evan Gillespie",)


class PPGui(object):
	"""
	class to create and handle the gui for pantone perfect
	"""

	def __init__(self):
		"""
		"""
		self.root = Tk()

		# make the root widget fullscreen
		w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
		self.root.overrideredirect(1)
		self.root.geometry("%dx%d+0+0" % (w, h))

		self.label = Label(
			self.root,
			text="LABEL",
			# hex color string. This does it: '#%02x%02x%02x' % (64, 204, 208)
			bg='#40E0D0',
			fg='#101010',
			anchor=SW,
		)
		self.label.bind("<Button-1>", self.take_picture_and_analyze) 
		self.label.pack(fill=BOTH, expand=1)


	def take_picture_and_analyze(self, event):
		bg_colors = [
			'#90E0D0',
			'#40E0FF',
			'#40E000',
			'#4012D0'
		]
		c = choice(bg_colors)
		self.label.config(bg=c, text=c)


	def get_root(self):
		return self.root