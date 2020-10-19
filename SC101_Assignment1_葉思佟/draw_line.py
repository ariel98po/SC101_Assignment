"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 20
window = GWindow()
x = 0
y = 0
count = 0

def main():
    onmouseclicked(hole_puncher)

def hole_puncher(event):
    global count, x, y, hole
    count += 1
    if count % 2 == 1:
        hole = GOval(SIZE, SIZE, x=event.x - SIZE/2, y=event.y - SIZE/2)
        hole.color = 'black'
        window.add(hole)
    else:
        line = GLine(hole.x, hole.y, event.x, event.y)
        window.add(line)
        window.remove(hole)






if __name__ == '__main__':
	main()
