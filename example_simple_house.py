from khd.minecraft import *

# This is where you are
steve = getMyPosition()

# This is how you use it
# house( positionX, positionY, positionZ, width, height, depth )
# You can also check how to customize your house in a file called buildings.py
# inside the folder khd/draw ;)
house( steve.x + 3, steve.y, steve.z, 7, 3, 5 )