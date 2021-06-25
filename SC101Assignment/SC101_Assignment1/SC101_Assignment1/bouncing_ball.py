"""
File: Bouncing ball
Name: 洪禎蔚
-------------------------
TODO: This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
click_times = 0


def main():
    """
    Add a ball into the window, then move it with constant VX and vy start from 0 when player clicked the mouse.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)
    onmouseclicked(drop)


def drop(m):
    # Response to the mouse-click only when the ball is at the start point
    if ball.x == (START_X - SIZE / 2):
        global click_times
        # Only response to the mouse-click for 3 times
        if click_times < 3:
            vy = 0
            while True:
                ball.move(VX, vy)
                if ball.x >= window.width:
                    window.add(ball, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)
                    break
                else:
                    if ball.y <= window.height - SIZE:
                        vy += GRAVITY
                    else:
                        vy = -vy * REDUCE
                pause(DELAY)
            click_times += 1


if __name__ == "__main__":
    main()
