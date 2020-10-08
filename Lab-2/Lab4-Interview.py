from sense_hat import SenseHat
import time

"""

  Sense HAT Initials Display
  
  Note: Requires sense_hat 2.2.0 or later

"""

sense = SenseHat()

green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


def show_c():
  sense.show_letter("T", back_colour = green)
  time.sleep(.5)

def show_m():
  sense.show_letter("A", back_colour = blue)
  time.sleep(.5)

####
# Intro Animation
####

show_c()
show_m()

c_selected = False

####
# Main game loop
####
count = 0

while True:
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":
      count += 1
      if c_selected:
         if count % 2:
            show_m()
            c_selected = False
      else:
          if count % 2:
            show_c()
            c_selected = True
  
  