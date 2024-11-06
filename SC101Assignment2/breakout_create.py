"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GLabel
from breakoutgraphics_create import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()
graphics.set_ball_velocity()


def main():
    graphics.paddle_move(graphics.paddle)
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    lives = NUM_LIVES
    graphics.score_label.font = '-25'
    graphics.window.add(graphics.score_label, x=5, y=graphics.window.height)
    while True:
        pause(FRAME_RATE)
        if graphics.start_click:
            graphics.ball.move(dx, dy)
            remove_brick(graphics.ball)
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.start_click = False
                graphics.reset_ball()
                graphics.window.add(graphics.ball)
                if lives == 0:
                    graphics.window.clear()
                    lose = GImage('lose.png')
                    graphics.window.add(lose, x=35, y=165)
                    word = GLabel("RRRRRRRRR")
                    word.font = '-20'
                    graphics.window.add(word, x=50, y=270)
                    word = GLabel("這什麼鬼遊戲 !")
                    word.font = '-20'
                    graphics.window.add(word, x=45, y=240)
                    break


def remove_brick(event):
    ball_left_top = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    ball_left_bottom = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
    ball_right_top = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
    ball_right_bottom = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)
    obj = graphics.window.get_object_at(event.x, event.y)
    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
        graphics.dx = -graphics.dx
    if graphics.ball.y <= 0:
        graphics.dy = -graphics.dy
    if obj == graphics.paddle:
        graphics.dy = - graphics.dy
    if obj is not graphics.paddle and obj is not None and obj is not graphics.score_label:
        graphics.count += 10
        graphics.score_label.text = 'Score: ' + str(graphics.count)
        if ball_right_bottom == obj:
            graphics.window.remove(obj)
            graphics.dy = - graphics.dy
        elif ball_left_bottom == obj:
            graphics.window.remove(obj)
            graphics.dy = - graphics.dy
        elif ball_right_top == obj:
            graphics.window.remove(obj)
            graphics.dy = - graphics.dy
        elif ball_left_top == obj:
            graphics.window.remove(obj)
            graphics.dy = - graphics.dy



    # Add the animation loop here!


if __name__ == '__main__':
    main()
