"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged, onmouseclicked

# This constant controls the size of the pen stroke
SIZE = 3

window = GWindow()


def main():
	onmousedragged(draw)
	onmouseclicked(draw)


def draw(m):
	stroke = GOval(SIZE, SIZE)
	stroke.filled = True
	stroke.fill_color = 'black'
	window.add(stroke, x=m.x - stroke.width / 2, y=m.y - stroke.height / 2)


if __name__ == '__main__':
	main()
