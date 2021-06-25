"""
File: Draw line
Name: 洪禎蔚
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants control the diameter of the circle
SIZE = 5

# Global variables
bg = GWindow()
# the times of mouseclick
n = 0
# the position of the circle's center
click_x = 0
click_y = 0


def main():
    """
    TODO: draw a circle for the odd clicks,
    then erase the circle as well as
    draw a line that starts from last click and ends at this click
    for the even clicks
    """
    onmouseclicked(circle_line)


def circle_line(m):
    global n, click_x, click_y
    # The even click
    if n % 2 == 0:
        click = GOval(SIZE, SIZE, x=m.x - SIZE/2, y=m.y - SIZE/2)
        bg.add(click)
        n += 1
        click_x = m.x - SIZE/2
        click_y = m.y - SIZE/2
    # The odd click
    else:
        line = GLine(click_x + SIZE / 2, click_y + SIZE / 2, m.x, m.y)
        click = bg.get_object_at(click_x + SIZE/2, click_y)
        bg.remove(click)
        bg.add(line)
        n += 1


if __name__ == "__main__":
    main()
