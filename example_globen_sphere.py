from khd.minecraft import *

# This is where you are
steve = getMyPosition()

ball = Sphere()
ball.material = WOOL
ball.position( steve.x, steve.y + 40, steve.z )
ball.size( 60, 60, 60 )
ball.draw()

# ball.clear()
