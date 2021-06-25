from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 300
ZONE_HEIGHT = 300
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):

        # Create window
        self.w = GWindow(width=window_width, height=window_height, title='Zone Game')
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.w.add(self.ball)

        # Create zone
        self.zone = GRect(zone_width, zone_height)
        self.w.add(self.zone, x=(self.w.width - self.zone.width) / 2, y=(self.w.height - self.zone.height) / 2)

        # Create ball and initialize velocity/position
        self.vx = MAX_SPEED
        self.vy = MIN_Y_SPEED

        # Class內使用要先呼叫自己出來! In class, self.method is required to access internal method
        self.set_ball_position()

        # Initialize mouse listeners
    def start(self):
        onmouseclicked(self)
        return True

    def set_ball_position(self):
        while True:
            rand_x = random.randrange(0, self.w.width - self.ball.width)
            rand_y = random.randrange(0, self.w.height - self.ball.height)
            if rand_x < self.zone.x - 5 or rand_x > self.zone.x + self.zone.width + 5:
                break
            if rand_y < self.zone.y - 5 or rand_y > self.zone.y + self.zone.height + 5:
                break
        self.ball.x = rand_x
        self.ball.y = rand_y

        pass
