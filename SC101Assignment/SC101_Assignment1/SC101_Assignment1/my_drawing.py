"""
File: My drawing
Name: 洪禎蔚
----------------------
TODO: To create a picture with ovals, rectangles and label.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: Literally busy to death...
    """
    bg = GWindow(width=500, height=400)
    face = GOval(300, 250, x=100, y=100)
    face.filled = True
    face.fill_color = 'beige'
    face.color = 'grey'
    reye1 = GOval(50, 50, x=150, y=220)
    reye1.filled = True
    reye1.fill_color = 'grey'
    reye1.color = 'grey'
    reye2 = GOval(30, 30, x=155, y=225)
    reye2.filled = True
    reye2.fill_color = 'white'
    reye2.color = 'grey'
    reye3 = GOval(10, 10, x=160, y=230)
    reye3.filled = True
    reye3.fill_color = 'grey'
    reye3.color = 'grey'
    leye1 = GOval(50, 50, x=300, y=220)
    leye1.filled = True
    leye1.fill_color = 'grey'
    leye1.color = 'grey'
    leye2 = GOval(30, 30, x=305, y=225)
    leye2.filled = True
    leye2.fill_color = 'white'
    leye2.color = 'grey'
    leye3 = GOval(10, 10, x=310, y=230)
    leye3.filled = True
    leye3.fill_color = 'grey'
    leye3.color = 'grey'
    mouth = GRect(120, 20, x=200, y=280)
    mouth.filled = True
    mouth.fill_color = 'grey'
    mouth.color = 'grey'
    label = GLabel('KILL ME...')
    label.font = '-30'
    label.color = 'grey'
    bg.add(face)
    bg.add(reye1)
    bg.add(reye2)
    bg.add(reye3)
    bg.add(leye1)
    bg.add(leye2)
    bg.add(leye3)
    bg.add(mouth)
    bg.add(label, x=500-label.width, y=400)


if __name__ == '__main__':
    main()
