from khd.minecraft import *

# This is where you are
steve = getMyPosition()

# This draws a small box of dirt
box = Box()
box.material = DIRT
box.position( steve.x, steve.y, steve.z + 2 )
box.size( 3, 3, 3 )
box.draw()