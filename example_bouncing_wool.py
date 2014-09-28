from khd.minecraft import *
from time import *

mypos = world.player.getPos()
mypos.x = int( mypos.x )
mypos.y = int( mypos.y )
mypos.z = int( mypos.z )


ball = Box()
ball.material = WOOL
ball.size( 1, 1, 1 )
ball.position( mypos.x, mypos.y, mypos.z )

position = 0
direction = 1

while True :
	ball.draw()
	sleep( 0.5 )
	if position >= mypos.y + 10 :
		direction = -1
	if position <= mypos.y :
		direction = 1
	position = position + direction
	ball.clear()
	ball.position(  mypos.x, position, mypos.z )
