"""
File: my_drawing.py
Name: 
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=1000, height=500, title='Circles')
    c1 = GOval(100, 100, x=100, y=150)
    c1.filled = True
    c1.fill_color = 'thistle'
    c2 = GOval(100, 100, x=200, y=150)
    c3 = GOval(100, 100, x=300, y=150)
    c4 = GOval(100, 100, x=150, y=50)
    c5 = GOval(100, 100, x=250, y=50)
    label = GLabel('Test', x=200, y=50)
    label.font = '-30'
    window.add(c1)
    window.add(c2)
    window.add(c3)
    window.add(c4)
    window.add(c5)
    window.add(label)
    triangle = GPolygon()
    triangle.add_vertex((100, 300))
    triangle.add_vertex((300, 300))
    triangle.add_vertex((200, 200))
    window.add(triangle)
    a1 = GArc(100, 300, 90, 180)
    a1.filled = True
    a1.fill_color = "blue"
    window.add(a1)


if __name__ == '__main__':
    main()
