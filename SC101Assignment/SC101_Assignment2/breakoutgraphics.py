"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-------------------------
File: breakout
Name: 洪禎蔚
-------------------------
TODO: Set up the original field of the game and create some function to execute it.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                            x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_ball)

        # Draw bricks
        self.brick_num = brick_cols * brick_rows
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j // 2 == 0:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j // 2 == 1:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j // 2 == 2:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j // 2 == 3:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))

    # Give ball a random x velocity and fixed y velocity after mouse clicked
    def start_ball(self, m):
        if self.__dx == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    # Track the mouse with the paddle
    def paddle_move(self, m):
        # Fixed y of paddle regardless of mouse
        self.paddle.y = self.window.height - self.paddle_offset
        # Limit the x of paddle inside the window
        if m.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif m.x < self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = m.x - self.paddle.width/2
        self.window.add(self.paddle)

    # Getter of dx
    def get_dx(self):
        return self.__dx

    # Getter of dy
    def get_dy(self):
        return self.__dy

    # Change the direction of the ball after bump into the walls
    def check_border(self):
        if self.ball.x < 0 or self.ball.x > (self.window.width - self.ball.width):
            self.__dx *= -1
        if self.ball.y < 0:
            self.__dy *= -1

    # Change the direction of the ball when bump into the stuff other than the wall
    def bumping(self):
        maybe_object_up = self.window.get_object_at(self.ball.x + self.ball.width/2 + 1, self.ball.y)
        maybe_object_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height/2 + 1)
        maybe_object_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height/2 + 1)
        maybe_object_down = self.window.get_object_at(self.ball.x + self.ball.width/2 + 1, self.ball.y + self.ball.height)

        # bump into the paddle
        if maybe_object_down is not None and maybe_object_down is self.paddle:
            # make sure it won't stick on the paddle
            self.__dy = -1 * abs(self.__dy)

        # bump into the bricks vertically
        elif maybe_object_up is not None and maybe_object_up is not self.paddle:
            self.__dy = -self.__dy
            self.window.remove(maybe_object_up)
            self.brick_num -= 1

        elif maybe_object_down is not None and maybe_object_down is not self.paddle:
            self.__dy = -self.__dy
            self.window.remove(maybe_object_down)
            self.brick_num -= 1

        # bump into the bricks horizontally
        elif maybe_object_right is not None and maybe_object_right is not self.paddle:
            self.__dx = -self.__dx
            self.window.remove(maybe_object_right)
            self.brick_num -= 1
            
        elif maybe_object_left is not None and maybe_object_left is not self.paddle:
            self.__dx = -self.__dx
            self.window.remove(maybe_object_left)
            self.brick_num -= 1
            
    # Change the y velocity when it goes downward
    def abs(self):
        if self.__dy > 0:
            self.__dy *= 1

    # Add the ball onto the middle of the window
    def add_ball(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.__dx = 0
        self.__dy = 0

    # Display 'game over' after the ball drops out of the window
    def game_over(self):
        game_over = GLabel('GAME OVER')
        game_over.filled = True
        game_over.font = 'Calibri-50'
        self.window.add(game_over, x=(self.window.width-game_over.width)/2, y=(self.window.height+game_over.height)/2)
        self.window.remove(self.ball)
        
    # To detect whether there is any brick left inside the window
    def no_bricks(self):
        if self.brick_num == 0:
            return True

    # Display 'you win' after all bricks cleared
    def win(self):
        win = GLabel('YOU WIN!!')
        win.filled = True
        win.font = 'Calibri-50'
        self.window.add(win, x=(self.window.width-win.width)/2, y=(self.window.height+win.height)/2)
        self.window.remove(self.ball)
