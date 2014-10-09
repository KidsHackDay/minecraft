from khd.minecraft import *
from time import *

# This is where you are
steve = getMyPosition()

ball = Box()
ball.material = WOOL
ball.size( 1, 1, 1 )
ball.position( steve.x, steve.y, steve.z + 2 )

position = steve.y
direction = 1

while True :
	ball.draw()
	sleep( 0.5 )
	if position >= steve.y + 10 :
		direction = -1
	if position <= steve.y :
		direction = 1
	position = position + direction
	ball.clear()
	ball.position( ball.x, position, ball.z )
