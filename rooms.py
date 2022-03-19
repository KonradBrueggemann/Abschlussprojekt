from room import Room
from objects import *

schlafzimmer = Room("Schlafzimmer", [hammer, streichholz])
wohnzimmer = Room("Wohnzimmer", [streichholz, pfefferspray])
badezimmer = Room("Badezimmer", [schluessel, gabel])
arbeitszimmer = Room("Arbeitszimmer", [axt], True)
flur = Room("Flur", [streichholz, handschuh, messer], False)
balkon = Room("Balkon", [streichholz, axt, wasserflasche], True)
