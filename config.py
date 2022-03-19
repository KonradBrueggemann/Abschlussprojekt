from map import Map
from rooms import *
from objects import *


# select objects you wish to be part of game (all objects are in objects.py file)
objects = [hammer, axt, pfefferspray, schluessel, streichholz, gabel, messer, handschuh, wasserflasche]

# Choose the object that needs to be acquired to win the game
needed_object = axt

# assign user inputs to object instances
object_map = {}
for obj in objects:
    object_map[f"{obj}".capitalize()] = obj

# Initiate Map as a matrix of nxm format
# Choose height and width
height = 3
width = 3

# map is being initiated
map1 = Map([[Room(f"Raum {str(x + 1)}") for x in range(width)] for x in range(height)])

# select the rooms you want
rooms = [schlafzimmer, flur, wohnzimmer, balkon, arbeitszimmer, badezimmer]


# Arrange rooms in map
# You can either do this manually (example below) or use the autofill method

### map1.set_room(0, 0, schlafzimmer)
### map1.set_room(1, 0, arbeitszimmer)
### ...

map1.autofill(height, width, rooms)
