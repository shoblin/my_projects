#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     12.09.2020
# Copyright:   (c) atopolskiy 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
import math

class Spiro:

    def __init__(self, xc, yc, col, R, r, l):

        #create the turtle  object
        self.t = turtle.Turtle()
        self.t.shape('turtle')

        #set the step in degrees
        self.step = 2
        #set the drawing complete flag
        self.drawingComplite = False

        #set parameters of spiro
        self.setparams(xc, yc, col, R,r, l)
        #Initialize the drawing
        self.restart()

    def setparams(self, xc, yc, col, R,r, l):
        #set center of the big circle
        self.xc = xc
        self.yc = yc

        #Set parameters of circles
        self.R = int(R)
        self.r = int(r)
        self.l = l # l=PC/r, PC - distance from center of little circle to point of pen
        self.col = col

        gcdVal = math.gcd(self.r, self.R)
        self.num_revol = self.r // gcdVal

        self.k = r / float(R)

        self.t.color(*col)

        self.angl = 0

    def restart(self):
        ''' Restart drawing'''
        #set the flag of drawing
        self.drawingComplite = False
        #
        self.t.showturtle()
        #go to start
        self.t.up()

        R, k, l = self.R, self.k, self.l
        a = 0.0

        # Set x, y of spiro
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)/k*a))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)/k*a))

        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def drawSpiro(self):
        R, k, l = self.R, self.k, self.l
        print(R, k, l)
        for i in range(0, 360*self.num_revol + 1, self.step):
            a = math.radians(i)

            # Set x, y of spiro
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        self.t.hideturtle()
        turtle.mainloop()



