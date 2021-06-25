"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 30

# This controls the pause time (in millisecond) for the animation
DELAY = 10


def main():
	window = GWindow()
	rect = set_up_rect()
	window.add(rect, (window.width-rect.width)/2, (window.height-rect.height)/2)
	vx = 5
	while True:
		rect.move(vx, 0)
		if rect.x <= 0 or (rect.x + rect.width) >= window.width:
			vx = -vx
		pause(DELAY)


def set_up_rect():
	rect = GRect(SIZE, SIZE)
	rect.filled = True
	rect.fill_color = 'magenta'
	rect.color = 'magenta'
	return rect

if __name__ == '__main__':
	main()
