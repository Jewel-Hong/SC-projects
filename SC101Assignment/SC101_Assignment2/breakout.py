"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
-------------------------
File: breakout
Name: 洪禎蔚
-------------------------
TODO: To show the set up filed of BreakoutGraphics, and move the ball after mouse clicked
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 30 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    num_lives = 0

    while True:
        # Update
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)

        # Check
        graphics.check_border()
        graphics.bumping()

        # Pause
        pause(FRAME_RATE)

        # Reset
        if graphics.ball.y > graphics.window.height:
            num_lives += 1
            graphics.add_ball()

        # End game
        if num_lives > NUM_LIVES - 1:
            graphics.game_over()
            break
        elif graphics.no_bricks():
            graphics.win()
            break


if __name__ == '__main__':
    main()
