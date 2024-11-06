"""
File: 
Name:黃方見
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved
SIZE = 20
circle = GOval(SIZE, SIZE)
# Global Variable
n = 0  # 點擊次數
x = 0
y = 0
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_line)


# 偶數畫圓圈，奇數畫直線
def create_line(mouse):
    global n, x, y
    if n % 2 == 0:
        x = mouse.x + SIZE//2
        y = mouse.y + SIZE//2
        hole = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
        window.add(hole)
        n += 1
    else:
        x1 = mouse.x
        y1 = mouse.y
        hole = window.get_object_at(x, y)  # 需要先延用偶數的第一個點
        window.remove(hole)
        line = GLine(x, y, x1, y1)
        window.add(line)
        n += 1


if __name__ == "__main__":
    main()
