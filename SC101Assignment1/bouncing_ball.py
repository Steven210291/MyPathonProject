"""
File: 
Name:
-------------------------
TODO:
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
open_gate = False

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global GRAVITY, VX, REDUCE, open_gate
    vy = 0  # Ｙ軸的力
    times = 0  # 總次數
    ball = bouncing_ball()
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start)
    while True:
        if open_gate:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y <= 0 or ball.y+ball.height >= window.height:
                if vy > 0:
                    vy = -vy * REDUCE
        if ball.x+ball.width >= window.width:
            window.add(ball, x=START_X, y=START_Y)
            open_gate = False
            times += 1
            vy = 0
        pause(DELAY)
        if times == 3:
            break


def bouncing_ball():
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    return ball


def start(mouse):
    global open_gate
    open_gate = True







if __name__ == "__main__":
    main()
