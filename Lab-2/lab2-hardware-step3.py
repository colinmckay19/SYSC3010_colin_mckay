from sense_hat import SenseHat
from random import randint
from time import sleep

"""
    This is a modification of the "Sense HAT random sparkles" tutorial found at:
    https://projects.raspberrypi.org/en/projects/sense-hat-random-sparkles/1
    
    This code creates random x, y and RGB values. However, a pixel is only set on the board
    if the x and y coordinates are in the shape of a 'C' (my first initial).
    The code exits when the 'C' is fully formed.
    
    Author: Colin McKay
    Date: September 27, 2020

"""


sense = SenseHat()
sense.clear()

locations_of_c = [(2,1),(3,1),(4,1),(1,2),(5,2),(1,3),(1,4),(1,5),(1,6),(5,6),(2,7),(3,7),(4,7)]
saved_locations = list()

while True:
    x = randint(0,7)
    y = randint(0,7)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    if (x,y) in locations_of_c:
        if (x,y) not in saved_locations:   
            saved_locations.append((x,y))
            sense.set_pixel(x,y,r,g,b)
    sleep(0.025)
    if len(saved_locations) == len(locations_of_c):
        break
    
