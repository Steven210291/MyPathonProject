"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        a = (window_width - paddle_width) // 2  # 擊球板寬位置
        b = (window_height - paddle_height) - paddle_offset  # 擊球板高位置
        self.paddle = GRect(paddle_width, paddle_height, x=a, y=b)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        c_w = window_width//2 - ball_radius  # 球中心位置
        c_h = window_height//2 - ball_radius  # 球中心位置
        self.ball = GOval(ball_radius*2, ball_radius*2, x=c_w, y=c_h)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        self.start_click = False
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.click)
        # Draw bricks
        for i in range(brick_rows+1):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=(brick_spacing+brick_width)*(i-1),
                                   y=brick_offset+(brick_spacing+brick_height)*(j-1))
                self.brick.filled = True
                self.brick.fill_color = "red"
                if j >= 2:
                    self.brick.filled = True
                    self.brick.fill_color = "orange"
                if j >= 4:
                    self.brick.filled = True
                    self.brick.fill_color = "yellow"
                if j >= 6:
                    self.brick.filled = True
                    self.brick.fill_color = "green"
                if j >= 8:
                    self.brick.filled = True
                    self.brick.fill_color = "blue"
                self.window.add(self.brick)

    def paddle_move(self, mouse):
        if mouse.x <= self.paddle.width // 2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width // 2

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def set_ball_velocity(self):
        self.dx = random.randint(1, MAX_X_SPEED)
        self.dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.dx = -self.dx

    def reset_ball(self):
        self.set_ball_velocity()
        self.window.add(self.ball, x=self.window.width//2 - self.ball.width, y=self.window.height//2 - self.ball.width)

    def click(self, mouse):
        self.start_click = True




