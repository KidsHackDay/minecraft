from khd.minecraft import *

# This draws a 3D line
line = Line()
line.material = STONE
line.begin( 0, 0, 0 )
line.end( 10, 10, 5)
line.draw()