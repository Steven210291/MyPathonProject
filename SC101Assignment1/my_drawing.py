"""
File: 
Name:黃方見

TODO:This is my favorite cartoon character
     Stupid dog usually scared by sudden occurrence
     but he always be cool to try bomb disposal ex:product manager
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title:My man

    This is my favorite cartoon character
    Stupid dog usually scared by sudden occurrence
    but he always be cool to try bomb disposal ex:product manager
    """
    window = GWindow(width=900, height=700, title='stupid dog')
    sun = GOval(100, 100, x=50, y=70)
    window.add(sun)
    sun.color = "yellow"
    sun.fill_color = "yellow"
    sun1 = GPolygon()
    sun1.add_vertex((160, 95))
    sun1.add_vertex((170, 115))
    sun1.add_vertex((160, 140))
    window.add(sun1)
    sun1.fill_color = 'yellow'
    sun2 = GPolygon()
    sun2.add_vertex((40, 95))
    sun2.add_vertex((30, 115))
    sun2.add_vertex((40, 140))
    window.add(sun2)
    sun2.fill_color = 'yellow'
    sun3 = GPolygon()
    sun3.add_vertex((83, 60))
    sun3.add_vertex((103, 50))
    sun3.add_vertex((123, 60))
    window.add(sun3)
    sun3.fill_color = 'yellow'
    sun4 = GPolygon()
    sun4.add_vertex((83, 180))
    sun4.add_vertex((103, 190))
    sun4.add_vertex((123, 180))
    window.add(sun4)
    sun4.fill_color = 'yellow'
    sun5 = GPolygon()
    sun5.add_vertex((158, 150))
    sun5.add_vertex((153, 165))
    sun5.add_vertex((138, 175))
    window.add(sun5)
    sun5.fill_color = 'yellow'
    sun6 = GPolygon()
    sun6.add_vertex((42, 150))
    sun6.add_vertex((48, 165))
    sun6.add_vertex((67, 175))
    window.add(sun6)
    sun6.fill_color = 'yellow'
    sun7 = GPolygon()
    sun7.add_vertex((76, 60))
    sun7.add_vertex((48, 65))
    sun7.add_vertex((42, 85))
    window.add(sun7)
    sun7.fill_color = 'yellow'
    sun8 = GPolygon()
    sun8.add_vertex((132, 60))
    sun8.add_vertex((148, 65))
    sun8.add_vertex((160, 85))
    window.add(sun8)
    sun8.fill_color = 'yellow'
    bg = GOval(250, 80, x=280, y=490)
    bg.color = 'white'
    bg.filled = 'True'
    bg.fill_color = 'maroon'
    window.add(bg)
    bg1 = GOval(180, 165, x=325, y=310)
    bg1.color = 'violet'
    bg1.filled = 'True'
    bg1.fill_color = 'violet'
    window.add(bg1)
    bg2 = GOval(95, 90, x=450, y=315)
    bg2.color = 'violet'
    bg2.filled = 'True'
    bg2.fill_color = 'violet'
    window.add(bg2)

    face = GOval(120, 120, x=350, y=260)
    window.add(face)
    face.fill_color = 'violet'
    face.color = True
    m = GOval(4, 4, x=515, y=364)
    m.filled = True
    window.add(m)
    m1 = GOval(4, 4, x=525, y=351)
    m1.filled = True
    window.add(m1)
    m2 = GOval(4, 4, x=535, y=364)
    m2.filled = True
    window.add(m2)
    m3 = GOval(4, 4, x=447, y=375)
    m3.filled = True
    window.add(m3)
    nose = GPolygon()
    nose.add_vertex((449, 360))
    nose.add_vertex((490, 388))
    nose.add_vertex((530, 335))
    window.add(nose)
    nose.filled = True
    nose.fill_color = 'black'
    mouth1 = GArc(190, 80, 180, 100)
    window.add(mouth1, x=360, y=325)
    mouth1.filled = True
    nose1 = GArc(70, 30, 120, 220)
    window.add(nose1, x=413, y=362)
    nose1.filled = True
    nose2 = GArc(50, 40, 220, 240)
    window.add(nose2, x=500, y=340)
    nose2.filled = True
    nose3 = GArc(280, 80, 0, 80)
    window.add(nose3, x=400, y=320)
    nose3.filled = True
    body = GOval(115, 120, x=340, y=390)
    body.filled = True
    body.fill_color = "violet"
    window.add(body)
    l_ear = GArc(230, 10, 180, 80)
    window.add(l_ear, x=332, y=240)
    l_ear.filled = True
    e = GPolygon()
    e.add_vertex((333, 243))
    e.add_vertex((353, 253))
    e.add_vertex((370, 243))
    window.add(e)
    e.filled = True
    l_ear1 = GArc(10, 70, 160, 100)
    window.add(l_ear1, x=370, y=230)
    l_ear1.filled = True
    r_ear = GArc(280, 30, 180, 80)
    window.add(r_ear, x=420, y=230)
    r_ear.filled = True
    e1 = GPolygon()
    e1.add_vertex((418, 238))
    e1.add_vertex((443, 253))
    e1.add_vertex((475, 243))
    window.add(e1)
    e1.filled = True
    r_ear1 = GArc(20, 150, 90, 80)
    window.add(r_ear1, x=415, y=237)
    r_ear1.filled = True
    l_eye = GOval(35, 55, x=388, y=275)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)
    l_eye1 = GOval(8, 15, x=401, y=295)
    l_eye1.filled = True
    window.add(l_eye1)
    l_eye2 = GOval(2, 2, x=404, y=299)
    l_eye2.color = 'white'
    l_eye2.filled = True
    l_eye2.fill_color = "white"
    window.add(l_eye2)
    r_eye = GOval(35, 55, x=435, y=272)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)
    r_eye1 = GOval(7, 14, x=444, y=294)
    r_eye1.filled = True
    r_eye1.filled_color = 'red'
    window.add(r_eye1)
    r_eye2 = GOval(1, 1, x=446, y=298)
    r_eye2.color = "white"
    r_eye2.filled = True
    r_eye2.fill_color = 'white'
    window.add(r_eye2)
    palm = GOval(10, 10, x=400, y=420)
    palm.filled = True
    window.add(palm)
    palm1 = GOval(10, 10, x=425, y=416)
    palm1.filled = True
    window.add(palm1)
    eyebrow = GPolygon()
    eyebrow.add_vertex((408, 273))
    eyebrow.add_vertex((415, 275))
    eyebrow.add_vertex((388, 285))
    window.add(eyebrow)
    eyebrow.filled = True
    eyebrow1 = GPolygon()
    eyebrow1.add_vertex((440, 273))
    eyebrow1.add_vertex((450, 270))
    eyebrow1.add_vertex((473, 285))
    window.add(eyebrow1)
    eyebrow1.filled = True
    r_hand = GArc(50, 40, 230, 180)
    window.add(r_hand, x=420, y=385)
    r_hand.filled = True
    r_hand1 = GArc(50, 40, 220, 180)
    window.add(r_hand1, x=425, y=395)
    r_hand1.filled = True
    l_hand = GArc(100, 80, 60, 80)
    window.add(l_hand, x=360, y=420)
    l_hand.filled = True
    l_hand1 = GArc(100, 80, 60, 80)
    window.add(l_hand1, x=360, y=428)
    l_hand1.filled = True
    arc = GArc(155, 155, 110, 110)
    window.add(arc, x=333, y=342)
    arc.filled = True
    arc1 = GArc(23, 19, 50, 190)
    window.add(arc1, x=347, y=330)
    arc1.filled = True
    r_toe = GOval(20, 10, x=365, y=530)
    r_toe.filled = True
    window.add(r_toe)
    r_toe1 = GOval(10, 20, x=370, y=530)
    r_toe1.filled = True
    window.add(r_toe1)
    r_leg = GRect(10, 40, x=370, y=500)
    r_leg.filled = True
    r_leg.fill_color = 'violet'
    window.add(r_leg)
    l_toe = GOval(20, 10, x=415, y=530)
    l_toe.filled = True
    window.add(l_toe)
    l_toe1 = GOval(10, 20, x=420, y=530)
    l_toe1.filled = True
    window.add(l_toe1)
    l_leg = GRect(10, 40, x=420, y=500)
    l_leg.filled = True
    l_leg.fill_color = 'violet'
    window.add(l_leg)
    l_hand = GArc(100, 80, 60, 80)
    window.add(l_hand, x=295, y=460)
    l_hand.filled = True
    word = GLabel("STUPID DOG !")
    word.font = '-80'
    window.add(word, x=210, y=150)
    pass


if __name__ == '__main__':
    main()
