"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

##CONSTANT
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

INITIAL_Y_SPEED = 5.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
FRAME_RATE = 1000 / 100 # 120 frames per second.
NUM_LIVES = 3

#Global Variables
paddle_offset = PADDLE_OFFSET
lives = NUM_LIVES

class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height,
                       x=(window_width-paddle_width)/2, y=window_height-(paddle_offset+paddle_height))
        self.paddle.color = 'black'
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2 - ball_radius)
        self.ball.color = 'black'
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        #Initialize our mouse listeners.
        onmousemoved(self.mouse_track)
        
        self.switch = True # True means you can start the game
        onmouseclicked(self.mouse_start)

        #Number of bricks
        self.n_brick = brick_cols * brick_rows

        #Draw bricks.

        for i in range(brick_rows):
            for j in range(brick_cols):
                bricks = GRect(width=BRICK_WIDTH, height=BRICK_HEIGHT,
                                  x = j * (brick_width+brick_spacing),
                                  y = i * (brick_height+brick_spacing) + brick_offset )
                bricks.color = 'black'
                bricks.filled = True
                if i % 10 == 0 or i % 10 == 1:
                    bricks.fill_color = 'red'
                if i % 10 == 2 or i % 10 == 3:
                    bricks.fill_color = 'orange'
                if i % 10 == 4 or i % 10 == 5:
                    bricks.fill_color = 'yellow'
                if i % 10 == 6 or i % 10 == 7:
                    bricks.fill_color = 'green'
                if i % 10 == 8 or i % 10 == 9:
                    bricks.fill_color = 'blue'

                self.window.add(bricks)

    def mouse_track(self, mouse):
        global paddle_offset

        if mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
        
        self.paddle.y = self.window.height-(paddle_offset + self.paddle.height)

    
    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)


    def handle_wall_collisions(self):
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    def mouse_start(self, event):
        global lives
        x_start = (self.window.width - self.ball.width) / 2
        y_start = (self.window.height - self.ball.height) / 2
        if self.switch == True and lives > 0 and self.n_brick > 0:
            self.switch = False
            while True:
                self.move_ball()
                self.handle_wall_collisions()
                self.hitting_check()
                if self.ball.y > self.window.height:
                    lives -= 1
                    self.switch = True
                    self.ball.x = x_start
                    self.ball.y = y_start
                    break

                elif self.n_brick == 0:
                    break

                pause(FRAME_RATE)
            

            
    #Check if any coordinate of the ball hit object and what it hits.
    def hitting_check(self):
        global paddle_offset
        # 4 position coordinates of ball

        ball_x_list = [self.ball.x, self.ball.x, self.ball.x + self.ball.width, self.ball.x + self.ball.width]
        ball_y_list = [self.ball.y, self.ball.y + self.ball.height, self.ball.y, self.ball.y + self.ball.height]
        i = 0
        while i < 4:
            maybe_sth = self.window.get_object_at(ball_x_list[i], ball_y_list[i])
            if maybe_sth is not None:
                if maybe_sth is self.paddle:                   
                    self.__dy = -INITIAL_Y_SPEED
                    break

                else:
                    self.n_brick -= 1
                    self.window.remove(maybe_sth)
                    self.__dy = -self.__dy
                    break
            if maybe_sth is None:
                i += 1






