from khd.minecraft import *

# This is where you are
steve = getMyPosition()

# This clean a box 30,30,30 from 0,0,0
box = Box();
box.position( steve.x, steve.y, steve.z )
box.size( 30, 30, 30 )
box.clear()
