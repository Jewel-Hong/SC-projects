"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30

# Global variable
window = GWindow()


def main():
	onmouseclicked(hole_puncher)		#關不掉的function


def hole_puncher(m):
	hole = GOval(SIZE, SIZE, x=m.x, y=m.y)
	hole.filled = True
	hole.fill_color = 'black'
	window.add(hole)


if __name__ == '__main__':
	main()
