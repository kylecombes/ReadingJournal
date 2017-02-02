""" A new encoding of the Roman alphabet. Letters are drawn
    using as few lines as possible.
"""

import math
import turtle
import time

def draw_a(t, height):
    l = height/sin(60)
    t.setheading(60)
    t.fd(l)
    t.rt(120)
    t.fd(l)

def draw_b(t, height):
    t.setheading(90)
    t.fd(height)
    w = height/math.sqrt(2)*sin(45)
    diag = height/math.sqrt(2)
    t.rt(135)
    t.fd(diag)
    t.rt(90)
    t.fd(diag)
    t.setheading(0)
    t.pu()
    t.fd(w)

def draw_c(t, height):
    t.setheading(0)
    w = height/math.sqrt(2)*sin(45)
    l = height/math.sqrt(2)
    t.pu()
    t.fd(w)
    t.pd()
    t.lt(135)
    t.fd(l)
    t.rt(90)
    t.fd(l)
    t.rt(135)
    t.pu()
    t.fd(height)
    t.pd()
    t.rt(90)

def draw_d(t, height):
    pass

def cos(theta):
    """ Calculate the cosine of an angle in degrees. """
    return math.cos(math.radians(theta))

def sin(theta):
    """ Calculate the sine of an angle in degrees. """
    return math.sin(math.radians(theta))

def draw_string(t,h,hs,s):
    """ Print out a string on the screen using the new alphabet.

        t: a Turtle to draw with
        h: the line height (pixels)
        hs: the horizontl space between letters (pixels)
        s: the string to print
    """
    t.pd()
    for c in s.lower():
        if c == 'a':
            draw_a(t,h)
        elif c == 'b':
            draw_b(t,h)
        elif c == 'c':
            draw_c(t,h)
        else:
            print('Unrecognized letter %s' % c)
            continue
        t.setheading(0)
        t.pu()
        t.fd(hs)
        t.pd()

letter_height = 20
bob = turtle.Turtle()
draw_string(bob, 20, 10, 'abc')
turtle.mainloop()
