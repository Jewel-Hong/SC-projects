"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# Constant controls the pause time of the animation
DELAY = 550

# Global variables
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
score = 0
score_label = GLabel('Score: ' + str(score))

# TODO:


def main():
    onmouseclicked(remove_mole)
    score_label.font = '-50'
    window.add(score_label, x=0, y=score_label.height)
    while True:
        mole = GImage('mole.png')
        mole.x = random.randint(0, window.width - mole.width)
        mole.y = random.randint(0, window.height - mole.height)
        window.add(mole)
        pause(DELAY)


def remove_mole(m):
    global score
    maybe_mole = window.get_object_at(m.x, m.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        score_label.text = 'Score: ' + str(score)



if __name__ == '__main__':
    main()
