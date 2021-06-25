"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 10


window = GWindow()
rect_t = GRect(SIZE, SIZE)


def main():
	rect_t.filled = True
	rect_t.fill_color = 'black'
	onmousemoved(track)
	onmouseclicked(draw)
	onmousedragged(draw)


def draw(m):
	rect_d = GRect(SIZE, SIZE)  #會做出很多個rect_d，但表示的是最後一個rect_d
	rect_d.filled = True
	rect_d.fill_color = 'black'
	window.add(rect_d, x=m.x - rect_d.width/2, y=m.y - rect_d.height/2)


def track(m):
	rect_t.x = m.x - rect_t.width/2
	rect_t.y = m.y - rect_t.height/2
	window.add(rect_t)


if __name__ == '__main__':
	main()
