from khd.minecraft import *

# This draws a small box of dirt
box = Box()
box.material = DIRT
box.position( 0, 5, 5 )
box.size( 3, 3, 3 )
box.draw()