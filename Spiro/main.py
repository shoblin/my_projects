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
import spiro
import random

def main():
    sp = spiro.Spiro(0, 0, (random.random(), random.random(), random.random()), 300, 85, 0.999)
    sp.drawSpiro()



if __name__ == '__main__':
    main()
