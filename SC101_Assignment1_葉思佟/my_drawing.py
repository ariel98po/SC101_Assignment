"""
File: 
Name:
----------------------
TODO:
"""


from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon
from campy.graphics.gwindow import GWindow

def main():
    window = GWindow(width=600, height=500, title='tsum tsum')


    """
    #1 Aliens
    """

    background = GRect(600, 500)
    background.filled = True
    background.fill_color = 'white'
    window.add(background)

    mickey_lear = GOval(150, 150, x=80, y=160)
    mickey_lear.color = 'black'
    mickey_lear.filled = True
    mickey_lear.fill_color = 'limegreen'
    window.add(mickey_lear)

    alien_cover_lear = GOval(150, 150, x=130, y=120)
    alien_cover_lear.color = 'white'
    alien_cover_lear.filled = True
    alien_cover_lear.fill_color = 'white'
    window.add(alien_cover_lear)

    alien_rear = GOval(150, 150, x=350, y=160)
    alien_rear.color = 'black'
    alien_rear.filled = True
    alien_rear.fill_color = 'limegreen'
    window.add(alien_rear)

    alien_cover_rear = GOval(150, 150, x=310, y=120)
    alien_cover_rear.color = 'white'
    alien_cover_rear.filled = True
    alien_cover_rear.fill_color = 'white'
    window.add(alien_cover_rear)

    alien_lhand = GOval(40, 40, x=180, y=380)
    alien_lhand.color = 'black'
    alien_lhand.filled = True
    alien_lhand.fill_color = 'limegreen'
    window.add(alien_lhand)

    alien_rhand = GOval(40, 40, x=380, y=380)
    alien_rhand.color = 'black'
    alien_rhand.filled = True
    alien_rhand.fill_color = 'limegreen'
    window.add(alien_rhand)

    alien_face = GOval(300, 270, x=150, y=150)
    alien_face.color = 'black'
    alien_face.filled = True
    alien_face.fill_color = 'limegreen'
    window.add(alien_face)

    alien_leye = GOval(70, 70, x=190, y=280)
    alien_leye.color = 'black'
    alien_leye.filled = True
    alien_leye.fill_color = 'white'
    window.add(alien_leye)

    alien_meye = GOval(70, 70, x=270, y=240)
    alien_meye.color = 'black'
    alien_meye.filled = True
    alien_meye.fill_color = 'white'
    window.add(alien_meye)

    alien_reye = GOval(70, 70, x=350, y=280)
    alien_reye.color = 'black'
    alien_reye.filled = True
    alien_reye.fill_color = 'white'
    window.add(alien_reye)

    lball = GOval(30, 30, x=220, y=310)
    lball.filled = True
    lball.fill_color = 'black'
    window.add(lball)

    mball = GOval(30, 30, x=290, y=275)
    mball.filled = True
    mball.fill_color = 'black'
    window.add(mball)

    rball = GOval(30, 30, x=360, y=310)
    rball.filled = True
    rball.fill_color = 'black'
    window.add(rball)

    b_triangle = GPolygon()
    b_triangle.add_vertex((290, 200))
    b_triangle.add_vertex((320, 200))
    b_triangle.add_vertex((305, 100))
    b_triangle.color = 'black'
    b_triangle.filled = True
    b_triangle.fill_color = 'limegreen'
    window.add(b_triangle)

    t_headline = GOval(30, 30, x=290, y=100)
    t_headline.color = 'black'
    t_headline.filled = True
    t_headline.fill_color = 'limegreen'
    window.add(t_headline)









if __name__ == '__main__':
	main()
