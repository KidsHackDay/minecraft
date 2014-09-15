from khd.minecraft import *
from time import *

# This will make a block bounce
box = Box();
box.position( 0, 0, 0 )
box.size( 11, 11, 11 )

ball = Box()
ball.material = WOOL
ball.size( 1, 1, 1 )
y = 0
vel = 1

while True :
	ball.draw()
	ball.position( 2, y, 2 )
	if y >= 10 :
		vel = -1
	if y <= 1 :
		vel = 1
	y += vel
	sleep( 0.5 )
	box.clear()